from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from django.http import JsonResponse
import json
from django.http import HttpResponse

# Create your views here.
class HelloAPIView(APIView):
    def get(self, request):
        a = 1
        return Response("HELLO!!!")

class UserAPIView(APIView):

    def post(self, request):
        # self.params["user_form"]
        data = json.loads(request.body)
        name = data.get('name')  # "title" パラメータを取得
        uid = data.get('uid')  
       
        sql = "INSERT INTO api_user (name, uid) VALUES (%s, %s)"

        print(name, uid)
        with connection.cursor() as cursor:
            cursor.execute(sql, [name, uid])

        return JsonResponse({"message": "Article saved successfully!"})
        
class PostAPIView(APIView):
    def post(self, request):
        date = json.loads(request.body) # リクエストからデータ取得
        title = date.get('title')
        uid = date.get('uid')
        content = date.get('content')

        sql = "INSERT INTO api_post (title, uid, content) VALUES (%s,%s,%s)"

        with connection.cursor() as cursor:
            cursor.execute(sql, [title, uid, content])

        return JsonResponse({"message": "Article saved sucsessfully"})
    
    def get(self, request):
        # curl -X GET "http://127.0.0.1:8000/api/post/?uid=kazu0521"　これがリクエスト
        # リクエストからクエリストリングを取得
        uid = request.GET.get('uid')

        # クエリで指定されたuidで記事を検索
        sql  = "select title, content from api_post where uid = %s"

        with connection.cursor() as cursor:
            # sqlを実行
            cursor.execute(sql, [uid])
            result = cursor.fetchone()
            # resultはタプル型
            title = result[0]
        # リターンする時はjsonに変換したい
        json_data = json.dumps({"result": title}, ensure_ascii=False)
        return HttpResponse(json_data, content_type="application/json")

    def put(self, request):
        date = json.loads(request.body)
        title = date.get('title')
        uid = date.get('uid')
        content = date.get('content')

        sql = "UPDATE api_post SET title = %s, content = %s WHERE uid = %s;"
        with connection.cursor() as cursor:
            cursor.execute(sql, [title, content, uid])

        return JsonResponse({"message": "Article saved successfully!"})
    
    def delete(self, request, id):
        sql = "DELETE FROM api_post WHERE id = %s;"
        with connection.cursor() as cursor:
            cursor.execute(sql, [id])

        print(id)
        return JsonResponse({"message": "Article saved successfully!"})
    
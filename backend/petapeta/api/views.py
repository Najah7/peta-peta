from django.shortcuts import render
from django.http import HttpResponse
import json 
from rest_framework import viewsets



def healthcheck(request):
    params ={
        "message": "Server is working"
    }
    #json形式の文字列を生成
    json_str = json.dumps(params)
    return HttpResponse(json_str)
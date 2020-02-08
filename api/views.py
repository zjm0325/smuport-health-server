from django.db.models import Count, Sum
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, mixins  # 搜索
from rest_framework.utils import json
from django.contrib.auth import authenticate, login, logout

from . import models
from . import serializers


class AuthView(APIView):

    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        user = request.data.get('username', '')
        pwd = request.data.get('password', '')
        user = authenticate(username=user, password=pwd)   # 验证用户名和密码
        if user is not None:
            login(request, user)    # 将登陆成功的返回的user对象传入，这样就可以记录下用户的登录状态，(在全局存储用户信息，在任何视图函数都可以取出来)，人家有什么参数就传什么
            return Response(
                {'err_code': 2000, 'msg': '', 'data': {1}}
            )
        else:
            return Response(
                {'err_code': -1000, 'msg': '', 'data': {}}
            )

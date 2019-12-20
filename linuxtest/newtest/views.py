import hashlib
import json
import time

from django.shortcuts import render
from django.views import View
from rest_framework.parsers import JSONParser, FormParser,FileUploadParser,MultiPartParser
from rest_framework.permissions import BasePermission
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework import  serializers
from .models import *
from  django.http import HttpResponse,JsonResponse
#from datetime import  timedelta,tzinfo
from datetime import timedelta,tzinfo
from rest_framework import serializers
# Create your views here.
#为用户进行加密


def encryption(user):
    ctime = str(time.time())
    m = hashlib.md5(bytes(user,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token =request._request.GET.get('token')
        token_obj = UserTokenModel.objects.filter(token=token).first()
        if not token_obj:
            raise AuthenticationFailed('用户认证失败')
        return (token_obj.user, token_obj)


class RegisterView(APIView):
    def post(self,request,*args,**kwargs):
        account=request._request.POST.get('account')
        password=request._request.POST.get('password')
        user=UserModel.objects.filter(account=account).first()
        if  user:
            data={'msg':'用户已存在'}
            return JsonResponse(data)
        else:
            UserModel.objects.create(account=account,password=password)
            return  JsonResponse({'msg':'用户创建成功'})


class LoginView(APIView):
    def post(self,request,*args,**kwargs):
        account = request._request.POST.get('account')
        password = request._request.POST.get('password')
        user=UserModel.objects.filter(account=account,password=password).first()
        if user:
            token = encryption(user.account) #自动生成token
            UserTokenModel.objects.update_or_create(user=user, defaults={'token': token})  # 用户登录后为用户创建或更新token
            return JsonResponse({'code':'1','msg': '用户登录成功'})
        else:
            return JsonResponse({'code': '0', 'msg': '用户登录失败'})

#获取所有用户信息
class GetAllUserInfo(APIView):
    authentication_classes = [MyAuthentication, ]

    def get(self,request,*args,**kwargs):
        users = UserModel.objects.all()
        ser = UserListSerializer(instance=users, many=True)

        return HttpResponse(
            json.dumps(ser.data))

#全部用户信息序列化


class UserListSerializer(serializers.Serializer):
    account = serializers.CharField()
    password=serializers.CharField()


class ChangeUserInfo(APIView):
    authentication_classes = [MyAuthentication, ]

    def post(self,request,*args,**kwargs):
        account = request._request.POST.get('account')
        oldpassword =request._request.POST.get('oldpassword')
        newpassword=request._request.POST.get('newpassword')
        user=UserModel.objects.filter(account=account,password=oldpassword).first()
        if user:
            user.password = newpassword
            user.save()
            return  JsonResponse({'msg':'修改成功'})
        else:
            return JsonResponse({'msg': '密码错误'})


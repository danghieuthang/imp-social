from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import  getInformationOfPost, getInformationOfUser
# Create your views here.
def create_response(success: bool, data: dict = None, error=None):
    return {"success": success, "data": data, "error": error}

@api_view(['GET'])
def get_post(request):
    url =request.GET.get("url")
    if url:
        post = getInformationOfPost(url=url)
        if post:
            return Response(status=status.HTTP_200_OK, data=create_response(True, post))
        return Response(status=status.HTTP_200_OK, data=create_response(False, None))
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def get_user(request):
    username = request.GET.get("username")
    if username:
        user = getInformationOfUser(username=username)
        if user:
            return Response(status=status.HTTP_200_OK, data=create_response(True,data= user))
        return Response(status=status.HTTP_200_OK, data=create_response(False, None))
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


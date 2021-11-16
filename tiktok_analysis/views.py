from copy import error
from .services import TiktokError, TiktokService
from .serializers import GetSumaryPostSerializer, VerifyTiktokUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status


def create_response(success: bool, data: dict = None, error=None):
    return {"success": success, "data": data, "error": error}


@api_view(['POST'])
def verify_titok_user(request):
    seriazlier = VerifyTiktokUserSerializer(data=request.data)
    if seriazlier.is_valid():
        titok_serivce = TiktokService()
        user = titok_serivce.verify_user(
            username=seriazlier.data["username"], hash_tag=seriazlier.data["hash_tag"])
        if user:
            return Response(status=status.HTTP_200_OK, data=create_response(True, user))
        return Response(status=status.HTTP_200_OK, data=create_response(False, None))
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user(request):
    username =request.GET.get("username")
    if username:
        titok_serivce = TiktokService()
        user = titok_serivce.get_user(username)
        if user:
            return Response(status=status.HTTP_200_OK, data=create_response(True, user))
        return Response(status=status.HTTP_200_OK, data=create_response(False, None))
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_items_of_user(request):
    username =request.GET.get("username")
    if username:
        titok_serivce = TiktokService()
        user = titok_serivce.get_list_post(username)
        if user:
            return Response(status=status.HTTP_200_OK, data=create_response(True, user))
        return Response(status=status.HTTP_200_OK, data=create_response(False, None))
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def get_summary_post(request):
    seriazlier = GetSumaryPostSerializer(data=request.data)
    if seriazlier.is_valid():
        titok_serivce = TiktokService() 
        data = titok_serivce.get_summary_post(
            url=seriazlier.data["url"], hashtags=seriazlier.data["hashtags"], username=seriazlier.data["username"])
        if data:
            if data and type(data)==type(TiktokError.HASH_TAG_NOT_CORRECT):
                return Response(status=status.HTTP_200_OK, data=create_response(False, error=data.value))
            return Response(status=status.HTTP_200_OK, data=create_response(True,data=data))
        return Response(status=status.HTTP_200_OK, data={False, None})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

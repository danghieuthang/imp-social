from .services import TiktokService
from .serializers import VerifyTiktokUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

def create_response(success:bool, data:dict):
    return {"success": success, "data": data}

@api_view(['POST'])
def verify_titok_user(request):
    seriazlier = VerifyTiktokUserSerializer(data=request.data)
    if seriazlier.is_valid():
        titok_serivce= TiktokService()
        user = titok_serivce.verify_user(username=seriazlier.data["username"], hash_tag=seriazlier.data["hash_tag"])
        if user:
            return Response(status=status.HTTP_200_OK, data=create_response(True, user))
        return Response(status=status.HTTP_200_OK, data={False, None})

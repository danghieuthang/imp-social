from rest_framework import serializers

class VerifyTiktokUserSerializer(serializers.Serializer):
    username= serializers.CharField(required=True, max_length=256)
    hash_tag= serializers.CharField(required=True, max_length=256)

    
class GetSumaryPostSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)
    hashtags = serializers.CharField(required=False, max_length=256)
    username = serializers.CharField(required=False, max_length=256)
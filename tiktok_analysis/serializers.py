from rest_framework import serializers

class VerifyTiktokUserSerializer(serializers.Serializer):
    username= serializers.CharField(required=True, max_length=256)
    hash_tag= serializers.CharField(required=True, max_length=256)
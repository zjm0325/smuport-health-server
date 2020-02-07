from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class CheckRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CheckRecord
        fields = "__all__"





from rest_framework import serializers
from core.models import Users


class UsersSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

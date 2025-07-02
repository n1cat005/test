from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields =('id', 'username', 'password', 'password_confirm', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data['email']
        )

        return user


class LoginSerializer(serializers.Serializer):

    class Meta:
        model = User

        username = serializers.EmailField(required=True)
        password = serializers.CharField(max_length=255, write_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username and password:

            user = authenticate(username=username, password=password)
            if user:
                data['user'] = user

            data['user'] = user

            return data



class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    def validate(self, data):
        user = self.context.get('request').user
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        password_confirm = data.get('password_confirm')

        if not user.check_password(old_password):
            raise serializers.ValidationError("Bu parol yanlisdir", code=400)

        if new_password != password_confirm:
            raise serializers.ValidationError("Bu parol dogru deyil", code=400)


        if len(new_password) < 8:
            raise serializers.ValidationError("bfsbfsbdsbsds",code=400)

        return data


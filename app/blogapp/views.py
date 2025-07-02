from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from . import serializers
from .models import Post, Comment
from .serializers import RegisterSerializer, PostSerializer, CommentSerializer, LoginSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'})
        return Response(serializer.errors)

class LoginView(APIView):


    def validate(self, data):

        if not User.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError("account not found")

        return data

    def get_jwt_token(self, data):

        user = authenticate(username=data["username"], password=data["password"])

        if not user:
            return {"message": "invalid credentials", "data": {}}

        refresh = RefreshToken.for_user(user)

        return {
            "message": "login success",
            "data": {"token": {"refresh": str(refresh),
            "access": str(refresh.access_token)}}}

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Logged out successfully'})



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

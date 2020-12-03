from rest_framework import generics
from rest_framework.response import Response
from .serializer import BlogSerializer
from .models import Blog
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class BlogCreateApi(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

class BlogApi(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

class BlogUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

class BlogDeleteApi(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
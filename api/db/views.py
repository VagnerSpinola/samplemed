import jwt

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User

from .models import Blog
from .serializers import BlogSerializer


class LoginAPIView(APIView):

    def post(self, request):
        data = jwt.decode(request.data.get("token"), "secret", algorithms=["HS256"])
        user = User.objects.get(username=data.get("username"))
        if user.check_password(data.get("password")):
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class BlogAPIView(APIView):

    def get(self, request):
        blog = Blog.objects.all()
        blog = BlogSerializer(blog, many=True)
        return Response({"blogs": blog.data})

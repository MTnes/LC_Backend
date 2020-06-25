from django.shortcuts import render
from django.contrib.auth.models import User
from main_app.models import Badge, Media_Content, Session, Questions_Mapping, Feedback, TestClass
from rest_framework import viewsets
from main_app.serializers import TestSerializer, MediaContentSerializer, UserSerializer, BadgeSerializer, SessionSerializer, QuestionMappingSerializer, FeedbackSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

# Create your views here.

class TestView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        test = TestClass.objects.all()
        serializer = TestSerializer(test, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TestView(viewsets.ModelViewSet):
#     queryset = TestClass.objects.all()
#     serializer_class = TestSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class MediaContentViewSet(viewsets.ModelViewSet):
    queryset = Media_Content.objects.all()
    serializer_class = MediaContentSerializer

class QuestionMappingViewSet(viewsets.ModelViewSet):
    queryset = Questions_Mapping.objects.all()
    serializer_class = QuestionMappingSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

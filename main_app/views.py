from django.shortcuts import render
from django.contrib.auth.models import User
from main_app.models import Badge, Media_Content, Session, Questions_Mapping, Feedback
from rest_framework import viewsets
from main_app.serializers import MediaContentSerializer, UserSerializer, BadgeSerializer, SessionSerializer, QuestionMappingSerializer, FeedbackSerializer

# Create your views here.
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

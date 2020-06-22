from django.shortcuts import render
from django.contrib.auth.models import User
from main_app.models import Badge, Profile, Badge_Allot, Media_Content , Session, Creative_Space, Questions_Mapping, Result_Session, Feedback
from rest_framework import viewsets
from main_app.serializers import MediaContentSerializer, UserSerializer, BadgeSerializer, ProfileSerializer, BadgeAllotSerializer, SessionSerializer, CreativeSpaceSerializer, QuestionMappingSerializer, ResultSessionSerializer, FeedbackSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class BadgeAllotViewSet(viewsets.ModelViewSet):
    queryset = Badge_Allot.objects.all()
    serializer_class = BadgeAllotSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class MediaContentViewSet(viewsets.ModelViewSet):
    queryset = Media_Content.objects.all()
    serializer_class = MediaContentSerializer
    # http_method_names = ['get','post']

class CreativeSpaceViewSet(viewsets.ModelViewSet):
    queryset = Creative_Space.objects.all()
    serializer_class = CreativeSpaceSerializer

class QuestionMappingViewSet(viewsets.ModelViewSet):
    queryset = Questions_Mapping.objects.all()
    serializer_class = QuestionMappingSerializer

class ResultSessionViewSet(viewsets.ModelViewSet):
    queryset = Result_Session.objects.all()
    serializer_class = ResultSessionSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

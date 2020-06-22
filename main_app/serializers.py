from rest_framework import serializers
from django.contrib.auth.models import User
from main_app.models import Media_Content,Badge, Profile, Badge_Allot, Session, Creative_Space, Questions_Mapping, Result_Session, Feedback

#
# class Base64ImageField(serializers.ImageField):
#     """
#     A Django REST framework field for handling image-uploads through raw post data.
#     It uses base64 for encoding and decoding the contents of the file.
#
#     Heavily based on
#     https://github.com/tomchristie/django-rest-framework/pull/1268
#
#     Updated for Django REST framework 3.
#     """
#
#     def to_internal_value(self, data):
#         from django.core.files.base import ContentFile
#         import base64
#         import six
#         import uuid
#
#         # Check if this is a base64 string
#         if isinstance(data, six.string_types):
#             # Check if the base64 string is in the "data:" format
#             if 'data:' in data and ';base64,' in data:
#                 # Break out the header from the base64 content
#                 header, data = data.split(';base64,')
#
#             # Try to decode the file. Return validation error if it fails.
#             try:
#                 decoded_file = base64.b64decode(data)
#             except TypeError:
#                 self.fail('invalid_image')
#
#             # Generate file name:
#             file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
#             # Get the file name extension:
#             file_extension = self.get_file_extension(file_name, decoded_file)
#
#             complete_file_name = "%s.%s" % (file_name, file_extension, )
#
#             data = ContentFile(decoded_file, name=complete_file_name)
#
#         return super(Base64ImageField, self).to_internal_value(data)
#
#     def get_file_extension(self, file_name, decoded_file):
#         import imghdr
#
#         extension = imghdr.what(file_name, decoded_file)
#         extension = "jpg" if extension == "jpeg" else extension
#
#         return extension

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']
        write_only_fields = ('password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class BadgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Badge
        fields = ['badge_name','image','min_score','max_score']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['user','level_reached','overall_score']

class BadgeAllotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Badge_Allot
        fields = ['user','badge']

# class PillarsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Pillars
#         fields = ['name']

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ['id',
                  'session_id',
                  'session_name',
                  'quality_focused',
                  'check_in_content',
                  'introduce_to_session',
                  'close_content',
                  'how_am_i_learning',
                  'achievements_today']

class MediaContentSerializer(serializers.HyperlinkedModelSerializer):
    media_content = serializers.FileField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = Media_Content
        fields = ['session','serial_number','media_content','text_content']


class CreativeSpaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Creative_Space
        fields = ['session','image','any_text']

class QuestionMappingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questions_Mapping
        fields = ['session','question_number','question','option_A','option_B','option_C','option_D','correct_answer']

class ResultSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result_Session
        fields = ['session','user','score']

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = ['session','feedback']

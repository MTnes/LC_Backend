from rest_framework import serializers
from django.contrib.auth.models import User
from main_app.models import Media_Content, Badge, Session, Questions_Mapping, Feedback, TestClass

from rest_framework import serializers

class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

class TestSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=64)
    doc = serializers.FileField(max_length=None, use_url=True)
    #
    # def create(self, validated_data):
    #     return TestClass.objects.create()
    class Meta:
        model = TestClass
        fields = ['doc']

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

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ['id',
                  'compitency',
                  'theme',
                  'name',
                  'index',
                  'introduction',
                  'moral',
                  'num_pages',
                  'date_uploaded']

class MediaContentSerializer(serializers.HyperlinkedModelSerializer):
    media_content = Base64ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Media_Content
        fields = ['session','serial_number','media_content','text_content', 'id_for_session']

class QuestionMappingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questions_Mapping
        fields = ['session','serial_number','id_for_session','question','option_A','option_B','option_C','option_D','correct_answer']

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = ['session','rating','feedback']

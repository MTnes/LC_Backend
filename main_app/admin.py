from main_app.models import Media_Content, Badge, Session, Questions_Mapping, Feedback, TestClass
from django.contrib import admin

# Register your models here.
admin.site.register(TestClass)
admin.site.register(Badge)
admin.site.register(Media_Content)
admin.site.register(Session)
admin.site.register(Questions_Mapping)
admin.site.register(Feedback)

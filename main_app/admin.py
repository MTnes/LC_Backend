from main_app.models import Media_Content, Badge, Profile, Badge_Allot, Session, Creative_Space, Questions_Mapping, Result_Session, Feedback
from django.contrib import admin

# Register your models here.
admin.site.register(Badge)
admin.site.register(Profile)
admin.site.register(Badge_Allot)
# admin.site.register(Pillars)
admin.site.register(Media_Content)
admin.site.register(Session)
admin.site.register(Creative_Space)
admin.site.register(Questions_Mapping)
admin.site.register(Result_Session)
admin.site.register(Feedback)

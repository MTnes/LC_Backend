from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from main_app import views
from rest_framework import routers
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'badge', views.BadgeViewSet)
router.register(r'badge_allot', views.BadgeAllotViewSet)
router.register(r'session', views.SessionViewSet)
router.register(r'creative_space', views.CreativeSpaceViewSet)
router.register(r'question_mapping', views.QuestionMappingViewSet)
router.register(r'result_session', views.ResultSessionViewSet)
router.register(r'feedback', views.FeedbackViewSet)
router.register(r'media_content', views.MediaContentViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('upload/', views.uploadClass.as_view())
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

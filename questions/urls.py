from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework import routers

from .views import *

# urlpatterns = [
#     # path('', ProfileDetail.as_view(), name='home'),
#     # path('', QuestionsAPIView.as_view({'get': 'list'})),
#     # path('', QuestionsAPIView.as_view()),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'question_groups', GroupsQuestionsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
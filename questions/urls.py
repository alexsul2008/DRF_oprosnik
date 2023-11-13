from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    # path('', ProfileDetail.as_view(), name='home'),
    path('', QuestionsAPIView.as_view({'get': 'list'})),
    # path('', QuestionsAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
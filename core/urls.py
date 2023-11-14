
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [

    path('', include('questions.urls')),
    path('admin/', admin.site.urls),
    # path('accounts/', include('rest_framework.urls')),
    # path('login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # path('accounts/', include('django.contrib.auth.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
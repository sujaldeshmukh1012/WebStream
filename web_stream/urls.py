from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("", include("video_stream.urls")),
    path("", include('django.contrib.auth.urls')),
    path("register", views.user_register)
]
# handler404 = 'web_stream.views.error_404'
# # handler500 = 'web_stream.views.error_500'

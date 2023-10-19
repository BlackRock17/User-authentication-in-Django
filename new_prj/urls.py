
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("new_prj.test_app.urls")),
    path("auth/", include("new_prj.app_auth.urls")),
]

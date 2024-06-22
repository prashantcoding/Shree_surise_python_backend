from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("imageStore/", include("imageStore.urls")),
    path("admin/", admin.site.urls),
]
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from oc_lettings_site import settings

from . import views

urlpatterns = [
    # re_path : All Urls wicht start by /static will be redirect here 
    # (debug css in mode Debug False (production))
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
]

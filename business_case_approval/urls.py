from django.contrib import admin
from django.urls import include, path

from business_case_approval.rbca import views

urlpatterns = [
    path("", views.page_view, name="pages-index"),
    path("<str:page_name>", views.page_view, name="pages"),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]

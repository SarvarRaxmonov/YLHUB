from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .schema import swagger_urlpatterns

urlpatterns = [
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("admin/", admin.site.urls),
    path("vebinars/", include("apps.vebinar.urls")),
    path("tests/", include("apps.student_test.urls")),
    path("user/", include("apps.user.urls")),
    path("main/", include("apps.main.urls")),
    path("notification/", include("apps.notification.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

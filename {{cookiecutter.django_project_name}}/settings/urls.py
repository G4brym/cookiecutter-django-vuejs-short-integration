from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from {{cookiecutter.django_project_name}}.apps.core.views import VuejsView

router = SimpleRouter()
# Register your api endpoints
# router.register("name", ViewSet)

urlpatterns = [
    # Vuejs view
    path("", VuejsView.as_view(), name="index"),

    # Internal api
    path("api/v1/", include(router.urls),),
]

if settings.DEBUG:
    import debug_toolbar
    from django.contrib import admin

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

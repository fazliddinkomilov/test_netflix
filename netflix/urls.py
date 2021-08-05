from django.contrib import admin
from django.urls import *
from movies.urls import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Movie Application Rest API",
        default_version="v1",
        description="Swagger docs for REST API",
        contact=openapi.Contact("Komilov Fazliddin <fazliddinkomilov777@gmail.com>")
    ),
    public=True,
    permission_classes=(AllowAny,)

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("movies.urls")),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger_docs"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name="re_doc"),

]

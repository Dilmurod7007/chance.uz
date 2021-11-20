from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from rest_framework_simplejwt import views as jwt_views



schema_view = get_schema_view(
    openapi.Info(
        title='Imkon API',
        terms_of_services="",
        default_version = 'v1',
        contact=openapi.Contact(email="a@gnail.com"),
        license=openapi.License(name="License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls', namespace='myapp')),
    path('', schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]





from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'homiylar', views.HomiyViewSet)
router.register(r'talabalar', views.TalabaViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'myapp'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
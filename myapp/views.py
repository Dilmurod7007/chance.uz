from rest_framework import viewsets

from .serializers import HomiySerializer, TalabaSerializer
from .models import Homiy, Talaba


class HomiyViewSet(viewsets.ModelViewSet):
    queryset = Homiy.objects.all().order_by('ismi')
    serializer_class = HomiySerializer




class TalabaViewSet(viewsets.ModelViewSet):
    queryset = Talaba.objects.all().order_by('ismi')
    serializer_class = TalabaSerializer



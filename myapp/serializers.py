from rest_framework import serializers

from .models import Homiy, Talaba

class HomiySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Homiy
        fields = ('id', 'ismi', 'turi', 'raqami', 'summa', 'tashkilot', 'holati', 'sarflangan_summa', 'created')



class TalabaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Talaba
        fields = ('id', 'ismi', 'talabalik_turi', 'otm', 'kontrakt_summa', 'ajratilgan_summa')


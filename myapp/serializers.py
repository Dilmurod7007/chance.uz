from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Contract, Sponsor, Student

from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as TokenObtainSerializer,
)


class SponsorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('id', 'name', 'personal', 'phone', 'amount', 'company', 'status', 'paid', 'created')


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'phone',
            'degree',
            'university',
            'money_needed',
            'money_gained',
            'created',
        )
        model = Student


class AddSponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ('sponsor', 'money')
        read_only_fields = ('created','updated')


    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['sponsor'] = SponsorSerializer(instance.sponsor).data
        return response


class TokenObtainSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(clc, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token



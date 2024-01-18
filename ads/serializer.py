from django.contrib.auth.models import User
from rest_framework import serializers

from ads.models import Advertisement, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class AdvertisementSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="advertisement-detail", lookup_field="pk"
    )

    class Meta:
        model = Advertisement
        fields = ["title", "description", "price", "publication_date", "url"]


class UserSerializer(serializers.ModelSerializer):
    advertisements = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Advertisement.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "advertisements"]

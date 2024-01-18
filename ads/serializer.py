from django.contrib.auth.models import User
from rest_framework import serializers

from ads.models import Advertisement, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class AdvertisementSerializer(serializers.ModelSerializer):
    category = CategorySerializer().read_only
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Advertisement
        fields = ["id", "title", "description", "price", "category", "owner"]


class UserSerializer(serializers.ModelSerializer):
    advertisements = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Advertisement.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "advertisements"]

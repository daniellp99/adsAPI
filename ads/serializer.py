from django.contrib.auth.models import User
from rest_framework import serializers

from ads.models import Advertisement, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class PublicationDateField(serializers.ReadOnlyField):
    def to_representation(self, value):
        return value.strftime("%B %d, %Y")


class AdvertisementSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="advertisement-detail", lookup_field="pk"
    )
    publication_date = PublicationDateField()

    class Meta:
        model = Advertisement
        fields = [
            "title",
            "description",
            "category",
            "price",
            "publication_date",
            "url",
        ]


class AdvertisementStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = [
            "status",
        ]


class AdvertisementDetailSerializer(serializers.ModelSerializer):
    publication_date = PublicationDateField()
    category = serializers.ReadOnlyField(source="category.name")
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Advertisement
        fields = [
            "title",
            "description",
            "price",
            "publication_date",
            "status",
            "owner",
            "category",
        ]
        read_only_fields = ["status"]


class UserSerializer(serializers.ModelSerializer):
    advertisements = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Advertisement.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "advertisements"]

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ads.models import Advertisement, Category, Comment


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["username"] = user.username
        # ...

        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


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
            "owner",
            "publication_date",
            "url",
        ]
        read_only_fields = ["owner"]

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().update(instance, validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    advertisements = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "advertisements"]


class AdvertisementModerationSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="advertisement-moderation-detail", lookup_field="pk"
    )
    publication_date = PublicationDateField()
    category = serializers.ReadOnlyField(source="category.name")
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Advertisement
        fields = [
            "title",
            "description",
            "category",
            "price",
            "publication_date",
            "owner",
            "url",
        ]


class AdvertisementStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = [
            "status",
        ]


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ["id", "text", "rating", "user"]


class AdvertisementDetailSerializer(serializers.ModelSerializer):
    publication_date = PublicationDateField()
    category = serializers.ReadOnlyField(source="category.name")
    owner = serializers.ReadOnlyField(source="owner.username")
    ratings = serializers.FloatField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

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
            "ratings",
            "comments",
        ]
        read_only_fields = ["status"]

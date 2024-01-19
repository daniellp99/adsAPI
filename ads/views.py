from django.contrib.auth.models import User
from rest_framework import generics, permissions

from ads.models import Advertisement, Category
from ads.permissions import IsOwnerOrReadOnly
from ads.serializer import (
    AdvertisementDetailSerializer,
    AdvertisementModerationSerializer,
    AdvertisementSerializer,
    AdvertisementStatusSerializer,
    CategorySerializer,
    UserSerializer,
)


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class AllAdvertisementList(generics.ListAPIView):
    queryset = Advertisement.objects.filter(status="A")
    serializer_class = AdvertisementSerializer
    permission_classes = [permissions.AllowAny]


class AdvertisementList(generics.ListCreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Advertisement.objects.filter(owner=self.request.user, status="D")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdvertisementModerationList(generics.ListAPIView):
    queryset = Advertisement.objects.filter(status="P")
    serializer_class = AdvertisementModerationSerializer
    permission_classes = [permissions.IsAdminUser]


class AdvertisementModerationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementModerationSerializer

    permission_classes = [IsOwnerOrReadOnly]


class AdvertisementPublish(generics.UpdateAPIView):
    queryset = Advertisement.objects.filter(status="D")
    serializer_class = AdvertisementStatusSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(status="P")


class AdvertisementApprove(generics.UpdateAPIView):
    queryset = Advertisement.objects.filter(status="P")
    serializer_class = AdvertisementStatusSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(status="A")


class AdvertisementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementDetailSerializer

    permission_classes = [IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

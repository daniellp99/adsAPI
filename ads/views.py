from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView


from ads.models import Advertisement, Category
from ads.permissions import IsOwnerOrReadOnly
from ads.serializer import (
    AdvertisementDetailSerializer,
    AdvertisementModerationSerializer,
    AdvertisementSerializer,
    AdvertisementStatusSerializer,
    CategorySerializer,
    MyTokenObtainPairSerializer,
    ProfileSerializer,
    RegisterSerializer,
)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Register User
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


# api/profile  and api/profile/update
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([permissions.IsAuthenticated])
def updateProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]


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

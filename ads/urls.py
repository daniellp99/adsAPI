from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from ads import views

urlpatterns = [
    # Authentication
    path("token/", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", views.RegisterView.as_view(), name="auth_register"),
    # Profile
    path("profile/", views.getProfile, name="profile"),
    path("profile/update/", views.updateProfile, name="update-profile"),
    # Category
    path("category/", views.CategoryList.as_view()),
    path("category/<int:pk>/", views.CategoryList.as_view()),
    # All Publish Ads
    path("advertisement/", views.AllAdvertisementList.as_view()),
    path(
        "advertisement/<int:pk>/",
        views.AdvertisementDetail.as_view(),
        name="advertisement-detail",
    ),
    path(
        "advertisement/<int:pk>/comment/",
        views.CommentCreateView.as_view(),
        name="ad_comment",
    ),
    # User Ads
    path("my-advertisements/", views.AdvertisementList.as_view()),
    path(
        "my-advertisements/<int:pk>/",
        views.AdvertisementDetail.as_view(),
        name="my-advertisements-detail",
    ),
    path("my-advertisements/<int:pk>/publish/", views.AdvertisementPublish.as_view()),
    path("pending-advertisement/", views.AdvertisementModerationList.as_view()),
    path(
        "pending-advertisement/<int:pk>/",
        views.AdvertisementModerationDetail.as_view(),
        name="advertisement-moderation-detail",
    ),
    path(
        "pending-advertisement/<int:pk>/approve/", views.AdvertisementApprove.as_view()
    ),
]

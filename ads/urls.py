from django.urls import path

from ads import views

urlpatterns = [
    path("user/", views.UserList.as_view()),
    path("user/<int:pk>/", views.UserDetail.as_view()),
    path("category/", views.CategoryList.as_view()),
    path("category/<int:pk>/", views.CategoryList.as_view()),
    path("advertisement/", views.AllAdvertisementList.as_view()),
    path(
        "advertisement/<int:pk>/",
        views.AdvertisementDetail.as_view(),
        name="advertisement-detail",
    ),
    path("my-advertisements/", views.AdvertisementList.as_view()),
    path(
        "my-advertisements/<int:pk>/",
        views.AdvertisementDetail.as_view(),
        name="advertisement-detail",
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

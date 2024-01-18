from django.urls import path

from ads import views

urlpatterns = [
    path("user/", views.UserList.as_view()),
    path("user/<int:pk>/", views.UserDetail.as_view()),
    path("category/", views.CategoryList.as_view()),
    path("category/<int:pk>/", views.CategoryList.as_view()),
    path("advertisement/", views.AdvertisementList.as_view()),
    path(
        "advertisement/<int:pk>/",
        views.AdvertisementDetail.as_view(),
        name="advertisement-detail",
    ),
]

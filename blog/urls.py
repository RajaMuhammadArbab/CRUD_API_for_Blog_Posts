from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path("posts/", views.PostListCreateView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),

    # Auth
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),          # 👈 added
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # 👈 added
]

from rest_framework.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.user.views import UserRegisterAPIView

urlpatterns = [
    path("register/", UserRegisterAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/token/", TokenRefreshView.as_view(), name="refresh-token"),
]

from django.urls import path
from .views import signup, verify_otp, login, verify_session, logout

urlpatterns = [
    path("auth/signup/", signup, name="signup"),
    path("auth/verify-otp/", verify_otp, name="verify-otp"),
    path("auth/login/", login, name="login"),
    path("auth/verify-session/", verify_session, name="verify-session"),
    path("auth/logout/", logout, name="logout"),
]

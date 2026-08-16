from django.urls import path
from .views import EmailTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import EmailTokenObtainPairView, CurrentUserView
from .views import CreateUserView

urlpatterns = [
    path('login/', EmailTokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("me/", CurrentUserView.as_view(), name="current-user"),
    path('users/', CreateUserView.as_view(), name='create-user'),
]
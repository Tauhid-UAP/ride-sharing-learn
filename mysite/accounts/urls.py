from django.urls import path
from .views import (
    UserCreateView,
    UserTokensView,
    # BecomeRider,
    # BecomeDriver,
    OnlyRider,
    OnlyDriver
)
from rest_framework_simplejwt.views import (
    TokenRefreshView
)

urlpatterns = [
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user_create_view/', UserCreateView.as_view(), name='user_create_view'),
    path('user_tokens_view/', UserTokensView.as_view(), name='user_tokens_view'),
    # path('become_rider/', BecomeRider.as_view(), name='become_rider'),
    # path('become_driver/', BecomeDriver.as_view(), name='become_drive'),
    path('only_rider/', OnlyRider.as_view(), name='only_rider'),
    path('only_driver/', OnlyDriver.as_view(), name='only_driver'),
]
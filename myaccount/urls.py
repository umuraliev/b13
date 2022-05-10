from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('sign_up/', RegisterView.as_view(), name="sign_up"),
    path('login/', SignInView.as_view(), name='login'),
    path('activate/<str:activation_code>/', activate, name='activate'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/',PasswordChange.as_view(), name='password_change'),
    path('password_change/done/',ChangeDone.as_view(),name='password_change_done'),
    path('password_reset/', PassReset.as_view(), name='password_reset'),
    path('password_reset/done/', PassResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PassResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', PassResetComplete.as_view(), name='password_reset_complete')
]

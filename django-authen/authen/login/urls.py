from django.urls import path
from .views import LoginClass, ViewUser

urlpatterns = [
    path('', LoginClass.as_view(), name="login"),
    path('user-view/', ViewUser.as_view(), name="user_view"),
]
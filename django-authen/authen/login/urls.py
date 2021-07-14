from django.urls import path
from .views import LoginClass, ViewUser, view_product, AddPost

app_name = 'Login'
urlpatterns = [
    path('', LoginClass.as_view(), name="login"),
    path('user-view/', ViewUser.as_view(), name="user_view"),
    path('view-product/', view_product, name="view-product"),
    path('add-post/', AddPost.as_view(), name="add_post"),
]
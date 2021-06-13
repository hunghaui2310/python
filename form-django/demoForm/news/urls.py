from django.urls import path
from . import views

app_name= 'news'
urlpatterns = [
    path('', views.index, name="index"),
    # path('add/', views.addPost, name="addPost"),
    path('save/', views.SavePost.as_view(), name="save"),
    path('email/', views.emailView, name="email"),
    path('receivedEmail/', views.receivedEmail, name="receivedEmail"),
    path('views/', views.IndexClass.as_view(), name="views"),
]
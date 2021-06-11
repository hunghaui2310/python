from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name="index"),
    path('list/', views.showAllQuestions, name='view_list'),
    path('abc/', views.ham1, name="ham"),
    path('detail/<int:question_id>/', views.detailView, name="detail"),
    path('<int:question_id>', views.submit, name="vote")
]
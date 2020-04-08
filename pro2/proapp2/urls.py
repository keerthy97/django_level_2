from django.conf.urls import url
from django.urls import path
from proapp2 import views

urlpatterns = [
    path('users/', views.users),
    path('index_1/', views.index_1),

]
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.show_blog, name='showblog'),
]


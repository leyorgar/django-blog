from django.urls import path
from . import views

# URL pattern
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
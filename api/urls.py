from django.urls import path
from .views import post_list,post_details

urlpatterns = [
    path('v1/post_list', post_list, name='post_list'),
    path('v1/post_details/<int:id>', post_details,name='post_details')
    
]
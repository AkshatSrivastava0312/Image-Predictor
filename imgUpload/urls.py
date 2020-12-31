from django.urls import path
from . import views

urlpatterns = [    
    path('', views.home, name='home'),
    path('postImg', views.post, name='post')
]

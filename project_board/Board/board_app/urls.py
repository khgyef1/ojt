from django.urls import path
from . import views

urlpatterns = [
    path('post', views.post, name='post'),
    path('', views.index, name='index'),
    path('post/<int:id>', views.detail, name='detail')
]

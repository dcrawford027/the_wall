from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall),
    path('post_message', views.postMessage),
    path('post_comment', views.postComment),
    path('delete_message', views.deleteMessage),
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('post/newpost',views.post_new,name='post_new'),
    path('post/<int:pk>/update',views.post_update,name='post_update'),
    path('post/<int:pk>/delete',views.post_delete,name='post_delete'),

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed_view, name='feed'),
    path('explore/', views.explore_view, name='explore'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('follow/<str:username>/', views.toggle_follow, name='toggle_follow'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', views.toggle_like, name='toggle_like'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]

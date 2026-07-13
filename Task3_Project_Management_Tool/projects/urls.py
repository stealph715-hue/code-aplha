from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('project/<int:project_id>/', views.project_board, name='project_board'),
    path('project/<int:project_id>/add-member/', views.add_member, name='add_member'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/status/', views.update_task_status, name='update_task_status'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('notifications/poll/', views.notifications_poll, name='notifications_poll'),
]

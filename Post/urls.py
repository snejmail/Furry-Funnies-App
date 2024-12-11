from django.urls import path

from Post import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.post_create, name='post_create'),
    path('<int:post_id>/details/', views.post_details, name='post_details'),
    path('<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('<int:post_id>/delete/', views.post_delete, name='post_delete'),
]
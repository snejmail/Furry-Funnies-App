from django.urls import path

from Author import views

urlpatterns = [
    path('create/', views.author_create, name='author_create'),
    path('details/', views.author_details, name='author_details'),
    path('edit/', views.author_edit, name='author_edit'),
    path('delete/', views.author_delete, name='author_delete'),
]

from django.contrib import admin
from django.urls import path
from posts import views
from users.views import lists

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('create/', views.create),
    path('update/', views.update),
    path('delete/', views.delete),
    path('users/', lists),
]

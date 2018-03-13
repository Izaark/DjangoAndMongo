
from django.contrib import admin
from django.urls import path
from users.views import UserViewSet
from posts.views import index, create, update, delete, PostListAPIView, PostCreateAPIView, lists, PostDetailAPIView, PostUpdateAPIView, PostDeleteAPIView

from rest_framework_mongoengine import routers
from django.conf.urls import include

# this is DRF router for REST API viewsets
router = routers.DefaultRouter()

router.register(r'user', UserViewSet, r'user')
router.register(r'list', lists, r'list')
# router.register(r'users', lists, r"users")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('create/', create),
    path('update/', update),
    path('delete/', delete),
    path('api/posts/list/', lists),
    path('api/posts/', PostListAPIView.as_view(), name='api'),
    path('api/posts/create/', PostCreateAPIView.as_view(), name='api'),
    path('api/posts/<slug:id>', PostDetailAPIView.as_view(), name='api'),
    path('api/posts/update/<slug:id>', PostUpdateAPIView.as_view(), name='api'),
    path('api/posts/delete/<slug:id>', PostDeleteAPIView.as_view(), name='api'),
    path('api/', include(router.urls), name='api'),
]

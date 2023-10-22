from django.urls import path, include

from rest_framework.routers import DefaultRouter

from posts.api.views import PostViewSet

router_posts = DefaultRouter()
router_posts.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router_posts.urls)),
]
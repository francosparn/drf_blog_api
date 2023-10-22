from django.urls import path, include

from rest_framework.routers import DefaultRouter

from comments.api.views import CommentViewSet

router_comments = DefaultRouter()
router_comments.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router_comments.urls))
]
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from categories.api.views import CategoryViewSet

router_categories = DefaultRouter()
router_categories.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router_categories.urls))
]
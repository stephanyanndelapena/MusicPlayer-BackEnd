from django.urls import path, include
from rest_framework import routers
from .views import TrackViewSet, PlaylistViewSet

router = routers.DefaultRouter()
router.register(r'tracks', TrackViewSet, basename='track')
router.register(r'playlists', PlaylistViewSet, basename='playlist')

urlpatterns = [
    path('', include(router.urls)),
]
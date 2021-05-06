from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'profile-view-set', views.ProfileViewSet)
router.register(r'post-view-set', views.PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('number-of-profiles/', views.number_of_profiles, name='number_of_profiles'),
    path('number-of-posts/', views.number_of_posts, name='number_of_posts'),
]

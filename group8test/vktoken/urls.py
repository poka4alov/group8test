from django.urls import path, include
from . import views

from rest_framework import routers
from . import views as vkviews

router = routers.DefaultRouter()
router.register('api/v1/vk_user', vkviews.VkUserViewSet)
router.register('api/v1/vk_token', vkviews.VkTokenViewSet)

urlpatterns = [
    path('', include(router.urls))
]

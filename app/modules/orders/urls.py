from django.urls import include, path
from rest_framework import routers
from .views import OrderViewSet, index

router = routers.DefaultRouter()
router.register(r'', OrderViewSet)

urlpatterns = [
    # path('', index, name='index'),
    path('', include(router.urls)),
]

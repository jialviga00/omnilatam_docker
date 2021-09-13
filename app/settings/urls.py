from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url
from custom.api.signin import api_signin, api_logout

urlpatterns = [
    path('customers/', include('modules.customers.urls')),
    path('orders/', include('modules.orders.urls')),
    path('signin/', api_signin, name='api_signin'),
    path('logout/', api_logout, name='api_logout'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

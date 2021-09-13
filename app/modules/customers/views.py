from .serializers import CustomerSerializer
from rest_framework import permissions
from rest_framework import viewsets
from .models import Customer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('creation_date')
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]
from .serializers import OrderSerializer, OrderDetailSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Order, OrderDetail
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the orders index.")


class OrderViewSet(viewsets.ModelViewSet):
    
    queryset = Order.objects.all().order_by('-order_date')
    serializer_class = OrderSerializer

    @action(detail=True, methods=['post', 'get'])
    def add_product(self, request, pk=None):
        
        self.serializer_class = OrderDetailSerializer
        order = self.get_object()
        data = request.data.copy()
        data['order'] = order.id
        serializer = OrderDetailSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def detail_order(self, request, pk=None):

        self.serializer_class = OrderDetailSerializer
        order = self.get_object()
        order_mvtos = OrderDetail.objects.filter(order=order)
        page = self.paginate_queryset(order_mvtos)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(order_mvtos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

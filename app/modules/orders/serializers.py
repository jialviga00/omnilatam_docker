from django.db.models import fields
from rest_framework import serializers
from .models import Order, OrderDetail


class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ['id', '__str__', 'customer', 'order_date']
		read_only_fields = ['id', 'order_date']

# HyperlinkedModelSerializer
class OrderDetailSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = OrderDetail
		fields = ['id', '__str__', 'order', 'product', 'amount', 'cant']
		read_only_fields = ['id']

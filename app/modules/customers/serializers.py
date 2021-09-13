from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','identification', 'name', 'address', 'creation_date']
        read_only_fields = ['id','creation_date']
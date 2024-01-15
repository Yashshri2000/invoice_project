from rest_framework import serializers
from .models import *


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id','date','customer_name']
    
    
class InvoiceDetailSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(read_only=True)
    class Meta:
        model = InvoiceDetail
        fields = ['invoice','quantity','unit_price','price','description']
        
  
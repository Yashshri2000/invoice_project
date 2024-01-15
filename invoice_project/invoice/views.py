from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from rest_framework import viewsets, permissions, status


# Create your views here.
class InvoiceList(APIView):
    def get_object(self, pk):
        try:
            return Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            raise Http404
        
    def get(self, request, pk=None, format=None):
        invoice = Invoice.objects.all()
        serializer= InvoiceSerializer(invoice, many=True)
        if pk:
            invoice = self.get_object(pk)
            serializer = InvoiceSerializer(invoice)
            return Response(serializer.data)
        else:
            return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, format=None):
        invoice = self.get_object(request.data['id'])
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class InvoiceDetailList(APIView):
    def get_object(self, pk):
        try:
            return InvoiceDetail.objects.get(invoice__pk=pk)
        except InvoiceDetail.DoesNotExist:
            raise Http404
        
    def get(self, request, pk=None, format=None):
        invoice = InvoiceDetail.objects.all()
        serializer= InvoiceDetailSerializer(invoice, many=True)
        if pk:
            invoice = self.get_object(pk)
            serializer = InvoiceDetailSerializer(invoice)
            return Response(serializer.data)
        else:
            return Response(serializer.data)
    
    def put(self, request, format=None):
        invoice = self.get_object(request.data['invoice']['id'])
        serializer = InvoiceDetailSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        invoice = self.get_object(pk)
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request,format=None):
        # print(request.data)
        invoice = Invoice.objects.get(pk=request.data['invoice']['id'])
        if invoice:
            existed_record = InvoiceDetail.objects.filter(invoice=invoice)
            if not existed_record:
                serializer = InvoiceDetailSerializer(data=request.data)            
                if serializer.is_valid():
                    serializer.validated_data['invoice']=invoice
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"massage":"record already exist!"})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
    

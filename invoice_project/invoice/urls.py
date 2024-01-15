from django.conf import settings
from django.urls import path

from . import views




urlpatterns = [
    path('invoices/', views.InvoiceList.as_view(), name='Invoice-list'),
    path('invoices/<int:pk>/', views.InvoiceList.as_view(), name='Invoice'),
    path('invoice/details/', views.InvoiceDetailList.as_view(), name='Invoice-detail-list'),
    path('invoice/details/<int:pk>/', views.InvoiceDetailList.as_view(), name='Invoice-Details'),

]
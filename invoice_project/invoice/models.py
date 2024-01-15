from django.db import models

# Create your models here.
class Invoice(models.Model):
    date = models.DateField(null=True, blank=True)
    customer_name = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return "{}-{}".format(self.customer_name, self.date)
    
class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, null=True, blank=True)
    description = models.TextField()
    quantity = models.FloatField()
    unit_price = models.FloatField()
    price = models.FloatField()
    
    
    

from django.db import models
from django.contrib.auth.models import AbstractUser

class EmployeeRecord(AbstractUser):
    fname = models.CharField(max_length=233, blank=True, null=True)
    lname = models.CharField(max_length=233, blank=True, null=True)
    email = models.CharField(max_length=233, blank=True, null=True, unique=True)
    duty = models.CharField(max_length=233, blank=True, null=True, unique=True)
    phone_number = models.CharField(max_length=233, blank=True, null=True, unique=True)

class SuppliersInventory(models.Model):
    supplier_name = models.CharField(max_length=233, blank=True, null=True)
    supplier_email = models.EmailField(max_length=233, blank=True, null=True)
    supplier_phone_number = models.CharField(max_length=233, blank=True, null=True)
    supplier_contact_address =  models.CharField(max_length=233, blank=True, null=True)
    date_enroll = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.supplier_name}"

class ProductsInventory(models.Model):
    product_name = models.CharField(max_length=233, blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_description = models.CharField(max_length=755, blank=True, null=True)
    product_quantity = models.PositiveBigIntegerField(default=0)
    product_supplier = models.ForeignKey(SuppliersInventory, on_delete=models.CASCADE)
    product_entry_staff = models.ForeignKey(EmployeeRecord, on_delete=models.CASCADE)
    entry_of_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name}"



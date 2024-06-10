from django.contrib import admin
from .models import ProductsInventory, SuppliersInventory, EmployeeRecord
# Register your models here.


class ProductInfoAdmin(admin.ModelAdmin):
    list_display =('id','product_name', 'entry_of_date','product_price','product_quantity','product_supplier','product_description', 'product_entry_staff')

admin.site.register(ProductsInventory, ProductInfoAdmin)


class SuppliersInfoAdmin(admin.ModelAdmin):
    list_display =('id','supplier_name', 'supplier_email','supplier_phone_number', 'supplier_contact_address')

admin.site.register(SuppliersInventory, SuppliersInfoAdmin)

class EmployeeInfoAdmin(admin.ModelAdmin):
    list_display =('id','fname', 'lname','email', 'duty', 'phone_number')

admin.site.register(EmployeeRecord, EmployeeInfoAdmin)
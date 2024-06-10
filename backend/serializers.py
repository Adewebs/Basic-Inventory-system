from rest_framework import serializers
from .models import ProductsInventory, SuppliersInventory, EmployeeRecord


class ProductInventorySerilizer(serializers.ModelSerializer):
    class Meta:

        model = ProductsInventory
        fields = '__all__'


class SupplierInventorySerilizer(serializers.ModelSerializer):
    class Meta:

        model = SuppliersInventory
        fields = '__all__'


class EmployeeSerilizer(serializers.ModelSerializer):
    class Meta:

        model = EmployeeRecord
        fields = '__all__'
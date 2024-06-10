import json
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout
from .models import ProductsInventory, SuppliersInventory, EmployeeRecord
from .serializers import ProductInventorySerilizer, SupplierInventorySerilizer, EmployeeSerilizer




@api_view(['POST'])
@permission_classes([AllowAny])
def create_product(request):
    data = json.loads(request.body)
    # safely grab form data  from request
    product_name = data.get("product_name")
    product_price  = data.get("product_price")
    product_description = data.get("product_description")
    product_quantity = data.get("product_quantity")
    product_supplier = data.get("product_supplier")
    product_entry_staff = data.get("product_staff")
    print(data)
    try:
        # check if importants paramenters aint empty
        if product_name is not None and product_price is not None and product_quantity is not None and product_supplier is not None and product_entry_staff is not None:

            try:
                # check for suppliers using ID
                check_supplier = SuppliersInventory.objects.get(id=product_supplier)

                # check for Staff using ID
                check_staff = EmployeeRecord.objects.get(id=product_entry_staff)

                # create Items in Db
                ProductsInventory.objects.create(
                    product_name=product_name,
                    product_price=product_price,
                    product_description=product_description,
                    product_quantity=product_quantity,
                    product_supplier=check_supplier,
                    product_entry_staff= check_staff

                )
                return Response({'status': True, 'message': "Items Successfully Added"},
                                status=status.HTTP_200_OK)


            except SuppliersInventory.DoesNotExist:
                return Response({'status': False, 'message': "missing important parameters"},
                                status=status.HTTP_400_BAD_REQUEST)




        else:
            return Response({'status': False, 'message': "missing important parameters"}, status=status.HTTP_400_BAD_REQUEST)



    except Exception as e:
        return Response({'status': False, 'message': "User Record Does Not Exist"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def add_suppliers(request):
    data = json.loads(request.body)
    # safely grab form data  from request
    supplier_name = data.get("supplier_name")
    supplier_email = data.get("supplier_email")
    supplier_phone_number = data.get("supplier_phone_number")
    supplier_contact_address = data.get("supplier_contact_address")

    # check if email field isnt empty
    if supplier_email is not None and supplier_name is not None:

        try:
            # check if suppliers already exist

            get_supplier = SuppliersInventory.objects.get(supplier_email = supplier_email)

            return Response({'status': False, 'message': "Suppliers Already Exist"},
                            status=status.HTTP_400_BAD_REQUEST)

        except SuppliersInventory.DoesNotExist:

            # create supplier record
            SuppliersInventory.objects.create(
                supplier_name = supplier_name,
                supplier_email = supplier_email,
                supplier_phone_number = supplier_phone_number ,
                supplier_contact_address = supplier_contact_address

            )

            return Response({'status': True, 'message': "Supplier Successfully Added"},
                            status=status.HTTP_200_OK)


    else:
        return Response({'status': False, 'message': "missing important parameters"},
                        status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
@permission_classes([AllowAny])
def edit_products(request):
    data = json.loads(request.body)
    # safely grab form data  from request
    product_id = data.get("product_id")
    product_name = data.get("product_name")
    product_price = data.get("product_price")
    product_description = data.get("product_description")
    product_quantity = data.get("product_quantity")
    product_supplier = data.get("product_supplier")

    # check if id is not none
    if product_id is not None:
        try:
            get_product_by_id = ProductsInventory.objects.get(id=product_id)
            get_supplier_by_id = SuppliersInventory.objects.get(id=product_supplier)
            
            # update product information
            
            get_product_by_id.product_name = product_name
            get_product_by_id.product_price = product_price
            get_product_by_id.product_description = product_description
            get_product_by_id.product_quantity = product_quantity
            get_product_by_id.product_supplier = get_supplier_by_id
            
            # save product
            get_product_by_id.save()
            
            return Response({'status': True, 'message': "Items Updated Successfully"},
                            status=status.HTTP_200_OK)

        except ProductsInventory.DoesNotExist:
            
            return Response({'status': False, 'message': "No product with this ID"},
                            status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'status': False, 'message': "Empty product ID"},
                        status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def edit_suppliers(request):
    data = json.loads(request.body)
    # safely grab form data  from request
    supplier_id = data.get("supplier_id")
    supplier_name = data.get("supplier_name")
    supplier_email = data.get("supplier_email")
    supplier_phone_number = data.get("supplier_phone_number")
    supplier_contact_address = data.get("supplier_contact_address")


    # check if id is not none
    if supplier_id is not None:
        try:
            get_supplier_by_id = SuppliersInventory.objects.get(id=supplier_id)

            # update Supplier information

            get_supplier_by_id.supplier_name = supplier_name
            get_supplier_by_id.supplier_email = supplier_email
            get_supplier_by_id.supplier_phone_number = supplier_phone_number
            get_supplier_by_id.supplier_contact_address = supplier_contact_address

            # save Supplier information
            get_supplier_by_id.save()

            return Response({'status': True, 'message': "Supplier Updated Successfully"},
                            status=status.HTTP_200_OK)

        except SuppliersInventory.DoesNotExist:

            return Response({'status': False, 'message': "No Supplier with this ID"},
                            status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'status': False, 'message': "Empty Supplier ID"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def list_all_products(request):
    get_all_products = ProductsInventory.objects.all()
    serializer = ProductInventorySerilizer (get_all_products, many=True)

    return Response({"status": True, "all_items": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def list_all_suppliers(request):
    get_all_suppliers = SuppliersInventory.objects.all()
    serializer = SupplierInventorySerilizer(get_all_suppliers, many=True)

    return Response({"status": True, "all_suppliers": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def delete_products(request):
    data = json.loads(request.body)
    # safely grab form data  from request
    product_id = data.get("product_id")

    # check if id is not none
    if product_id is not None:
        try:
            get_product_by_id = ProductsInventory.objects.get(id=product_id)

            # Delete product

            get_product_by_id.delete()

            return Response({'status': True, 'message': "Items Deleted Successfully"},
                            status=status.HTTP_200_OK)

        except ProductsInventory.DoesNotExist:

            return Response({'status': False, 'message': "No product with this ID"},
                            status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'status': False, 'message': "Empty product ID"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def delete_suppliers(request):

    data = json.loads(request.body)
    # safely grab form data  from request
    supplier_id = data.get("supplier_id")

    # check if id is not none

    if supplier_id is not None:
        try:
            get_supplier_by_id = SuppliersInventory.objects.get(id=supplier_id)


            # delete Supplier information
            get_supplier_by_id.delete()

            return Response({'status': True, 'message': "Supplier Deleted Successfully"},
                            status=status.HTTP_200_OK)

        except SuppliersInventory.DoesNotExist:

            return Response({'status': False, 'message': "No Supplier with this ID"},
                            status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'status': False, 'message': "Empty Supplier ID"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def list_all_employee(request):
    data = json.loads(request.body)

    # get all employee at the db
    get_all_employee = EmployeeRecord.objects.all()
    serializer = EmployeeSerilizer(get_all_employee, many=True)

    return Response({"status": True, "all_employee": serializer.data}, status=status.HTTP_200_OK)




from django.urls import path
from . import views

urlpatterns = [
    path('add_items/', views.create_product, name='add_items'),
    path('add_suppliers/', views.add_suppliers, name='add_suppliers'),
    path('update_items/', views.edit_products, name='update_items'),
    path('update_supplier/', views.edit_suppliers, name='update_supplier'),
    path('list_items/', views.list_all_products, name='list_items'),
    path('list_suppliers/', views.list_all_suppliers, name='list_suppliers'),
    path('delete_items/', views.delete_products, name='delete_items'),
    path('delete_supplier/', views.delete_suppliers, name='delete_supplier'),
    path('all_employee/', views.list_all_employee, name='all_employee'),
]
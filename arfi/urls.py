from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Revenue
    path('clients', views.clients_view, name='clients'),
    path('service_orders', views.service_orders_view, name='service_orders_view'),
    path('job_orders', views.job_orders_view, name='job_orders_view'),
    path('service_bills', views.service_bills_view, name='service_bills_view'),
    path('budget_plans', views.budget_plans_view, name='budget_plans_view'),
    # Expenditure
    path('purchase_orders', views.purchase_orders_view, name='purchase_orders_view'),
    path('items', views.items_view, name='items_view'),
    path('receiving_reports', views.receiving_reports_view, name='receiving_reports_view'),
    path('payment_receipts', views.payment_receipts_view, name='payment_receipts_view'),
]
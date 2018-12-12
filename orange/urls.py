"""orange URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from arfi.view_sets import *
from arfi.admin import admin_site
import arfi

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# Revenue
router.register('clients', ClientViewSet)
router.register('mandors', MandorViewSet)
router.register('job_orders', JobOrderViewSet)
router.register('service_orders', ServiceOrderViewSet)
router.register('service_bills', ServiceBillViewSet)
router.register('budget_plans', BudgetPlanViewSet)

# Expenditure
router.register('transactions', TransactionViewSet)
router.register('purchase_orders', PurchaseOrderViewSet)
router.register('items', ItemViewSet)
router.register('receiving_reports', ReceivingReportViewSet)
router.register('payment_receipts', PaymentReceiptViewSet)
router.register('suppliers', SupplierViewSet)

urlpatterns = [
    path('', include('arfi.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin_site.urls),
    path('admin-django/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

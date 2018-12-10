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
import arfi

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# Revenue
router.register('clients', ClientViewSet)
router.register('mandor', MandorViewSet)
router.register('job_order', JobOrderViewSet)
router.register('service_order', ServiceOrderViewSet)
router.register('service_bill', ServiceBillViewSet)
router.register('budget_plan', BudgetPlanViewSet)

# Expenditure
router.register('purchase_order', PurchaseOrderViewSet)
router.register('item', ItemViewSet)
router.register('receiving_report', ReceivingReportViewSet)
router.register('payment_receipt', PaymentReceiptViewSet)
router.register('supplier', SupplierViewSet)

urlpatterns = [
    path('', include('arfi.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

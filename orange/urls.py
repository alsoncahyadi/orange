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
from arfi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# Revenue
router.register('clients', views.ClientViewSet)
router.register('mandor', views.MandorViewSet)
router.register('job_order', views.JobOrderViewSet)
router.register('service_order', views.ServiceOrderViewSet)
router.register('service_bill', views.ServiceBillViewSet)
router.register('budget_plan', views.BudgetPlanViewSet)

# Expenditure
router.register('purchase_order', views.PurchaseOrderViewSet)
router.register('inventory_list', views.ItemViewSet)
router.register('receiving_report', views.ReceivingReportViewSet)
router.register('payment_receipt', views.PaymentReceiptViewSet)
router.register('supplier', views.SupplierViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('arfi/', include('arfi.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

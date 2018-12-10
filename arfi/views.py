from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User, Group
from arfi.serializers import *
from rest_framework import viewsets
from arfi.models import *

# Create your views here.
def index(request):
  return HttpResponse("Hello, world. You're at the polls index.")

class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer

# Revenue
class ClientViewSet(viewsets.ModelViewSet):
  queryset = Client.objects.all()
  serializer_class = ClientSerializer

class MandorViewSet(viewsets.ModelViewSet):
  queryset = Mandor.objects.all()
  serializer_class = MandorSerializer

class JobOrderViewSet(viewsets.ModelViewSet):
  queryset = JobOrder.objects.all()
  serializer_class = JobOrderSerializer

class ServiceOrderViewSet(viewsets.ModelViewSet):
  queryset = ServiceOrder.objects.all()
  serializer_class = ServiceOrderSerializer

class ServiceBillViewSet(viewsets.ModelViewSet):
  queryset = ServiceBill.objects.all()
  serializer_class = ServiceBillSerializer

class BudgetPlanViewSet(viewsets.ModelViewSet):
  queryset = BudgetPlan.objects.all()
  serializer_class = BudgetPlanSerializer

# Expenditure
class PurchaseOrderViewSet(viewsets.ModelViewSet):
  queryset = PurchaseOrder.objects.all()
  serializer_class = PurchaseOrderSerializer

class ItemViewSet(viewsets.ModelViewSet):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer

class ReceivingReportViewSet(viewsets.ModelViewSet):
  queryset = ReceivingReport.objects.all()
  serializer_class = ReceivingReportSerializer

class PaymentReceiptViewSet(viewsets.ModelViewSet):
  queryset = PaymentReceipt.objects.all()
  serializer_class = PaymentReceiptSerializer

class SupplierViewSet(viewsets.ModelViewSet):
  queryset = Supplier.objects.all()
  serializer_class = SupplierSerializer


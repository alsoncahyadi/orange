from django.contrib.auth.models import User, Group
from rest_framework import serializers as s
from arfi.models import *
from django.conf import settings
from rest_framework import pagination
from rest_framework.response import Response

class MyPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })

# Serializers define the API representation.
# Revenue
class UserSerializer(s.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'username', 'email', 'is_staff')

        
class ClientSerializer(s.ModelSerializer):
  class Meta:
    model = Client
    fields = '__all__'


class MandorSerializer(s.ModelSerializer):
  class Meta:
    model = Mandor
    fields = '__all__'


class JobOrderSerializer(s.ModelSerializer):
  class Meta:
    model = JobOrder
    fields = '__all__'


class ServiceOrderSerializer(s.ModelSerializer):
  class Meta:
    model = ServiceOrder
    fields = '__all__'


class ServiceBillSerializer(s.ModelSerializer):
  class Meta:
    model = ServiceBill
    fields = '__all__'


class BudgetPlanSerializer(s.ModelSerializer):
  class Meta:
    model = BudgetPlan
    fields = '__all__'


# Expenditure
class PurchaseOrderSerializer(s.ModelSerializer):
  class Meta:
    model = PurchaseOrder
    fields = '__all__'

    
class ItemSerializer(s.ModelSerializer):
  class Meta:
    model = Item
    fields = '__all__'

    
class ReceivingReportSerializer(s.ModelSerializer):
  class Meta:
    model = ReceivingReport
    fields = '__all__'

    
class PaymentReceiptSerializer(s.ModelSerializer):
  class Meta:
    model = PaymentReceipt
    fields = '__all__'

    
class SupplierSerializer(s.ModelSerializer):
  class Meta:
    model = Supplier
    fields = '__all__'

    
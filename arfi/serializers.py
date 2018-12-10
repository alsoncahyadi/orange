from django.contrib.auth.models import User, Group
from rest_framework import serializers as s
from arfi.models import *
from django.conf import settings
from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.fields import SerializerMethodField


class MyModelSerializer(s.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(MyModelSerializer, self).__init__(*args, **kwargs)

        if 'labels' in self.fields:
            raise RuntimeError(
                'You cant have labels field defined '
                'while using MyModelSerializer'
            )

        self.fields['labels'] = SerializerMethodField()

    def get_labels(self, *args):
        labels = {}

        for field in self.Meta.model._meta.get_fields():
            if field.name in self.fields:
                labels[field.name] = field.verbose_name

        return labels

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

        
class ClientSerializer(MyModelSerializer):
  class Meta:
    model = Client
    fields = '__all__'


class MandorSerializer(MyModelSerializer):
  class Meta:
    model = Mandor
    fields = '__all__'


class JobOrderSerializer(MyModelSerializer):
  class Meta:
    model = JobOrder
    fields = '__all__'


class ServiceOrderSerializer(MyModelSerializer):
  class Meta:
    model = ServiceOrder
    fields = '__all__'


class ServiceBillSerializer(MyModelSerializer):
  class Meta:
    model = ServiceBill
    fields = '__all__'


class BudgetPlanSerializer(MyModelSerializer):
  class Meta:
    model = BudgetPlan
    fields = '__all__'


# Expenditure
class PurchaseOrderSerializer(MyModelSerializer):
  class Meta:
    model = PurchaseOrder
    fields = '__all__'

    
class ItemSerializer(MyModelSerializer):
  class Meta:
    model = Item
    fields = '__all__'

    
class ReceivingReportSerializer(MyModelSerializer):
  class Meta:
    model = ReceivingReport
    fields = '__all__'

    
class PaymentReceiptSerializer(MyModelSerializer):
  class Meta:
    model = PaymentReceipt
    fields = '__all__'

    
class SupplierSerializer(MyModelSerializer):
  class Meta:
    model = Supplier
    fields = '__all__'

    
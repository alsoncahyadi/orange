from django.contrib.auth.models import User, Group
from rest_framework import serializers as s
from arfi.models import *
from django.conf import settings
from django.forms import model_to_dict
from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.fields import SerializerMethodField
from datetime import datetime

class MyModelSerializer(s.ModelSerializer):
  def __init__(self, *args, **kwargs):
    super(MyModelSerializer, self).__init__(*args, **kwargs)

    if 'labels' in self.fields:
      raise RuntimeError(
          'You cant have labels field defined '
          'while using MyModelSerializer'
      )

    # self.fields['labels'] = SerializerMethodField()

  def get_labels(self, *args):
    labels = {}

    for field in self.Meta.model._meta.get_fields():
      if field.name in self.fields:
        labels[field.name] = field.verbose_name

    return labels


class MyPagination(pagination.PageNumberPagination):

    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

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


class MandorReturnableMixin():

  def get_mandor(self, object):
    try:
      serialized = MandorSerializer(data=object.mandor_id.__dict__)
      serialized.is_valid()
      return serialized.validated_data
    except:
      return None

  def get_mandor_id__name(self, object):
    try:
      return object.mandor_id.name
    except:
      return None


class ClientReturnableMixin():

  def get_client(self, object):
    try:
      serialized = ClientSerializer(data=object.client_id.__dict__)
      serialized.is_valid()
      return serialized.validated_data
    except:
      return None

  def get_client_id__name(self, object):
    try:
      return object.client_id.name
    except:
      return None


class SupplierReturnableMixin():

  def get_supplier(self, object):
    try:
      serialized = SupplierSerializer(data=object.supplier_id.__dict__)
      serialized.is_valid()
      return serialized.validated_data
    except:
      return None

  def get_supplier_id__name(self, object):
    try:
      return object.supplier_id.name
    except:
      return None

class ItemsReturnableMixin():

  def get_items_raw(self, object):
    try:
      serialized = ItemSerializer(object.items.all(), many=True)
      return serialized.data
    except:
      None

  def get_items__name(self, object):
    try:
      serialized = ItemSerializer(object.items.all(), many=True)
      data = ", ".join(["{} ({}x)".format(datum["name"], datum["quantity"]) for datum in serialized.data])
      return data
    except:
      None


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


class JobOrderSerializer(MyModelSerializer, MandorReturnableMixin):
  mandor = s.SerializerMethodField()
  mandor_id__name = s.SerializerMethodField()
  date = s.DateTimeField(format="%A, %d %B %Y %I:%M%p")

  class Meta:
    model = JobOrder
    fields = '__all__'


class ServiceOrderSerializer(MyModelSerializer, ClientReturnableMixin):
  client = s.SerializerMethodField()
  client_id__name = s.SerializerMethodField()
  date = s.DateTimeField(format="%A, %d %B %Y %I:%M%p")

  class Meta:
    model = ServiceOrder
    fields = '__all__'


class ServiceBillSerializer(MyModelSerializer, ClientReturnableMixin):
  client = s.SerializerMethodField()
  client_id__name = s.SerializerMethodField()
  date = s.DateTimeField(format="%A, %d %B %Y %I:%M%p")

  class Meta:
    model = ServiceBill
    fields = '__all__'


class BudgetPlanSerializer(MyModelSerializer):
  total = s.SerializerMethodField()

  class Meta:
    model = BudgetPlan
    fields = '__all__'

  def get_total(self, budget_plan):
    # TODO
    return budget_plan.amount


# Expenditure
class TransactionSerializer(MyModelSerializer):
  class Meta:
    model = Transaction
    fields = '__all__'

class ItemSerializer(MyModelSerializer):
  updated_at = s.DateTimeField(format="%A, %d %B %Y %I:%M%p")
  
  class Meta:
    model = Item
    fields = '__all__'


class PurchaseOrderSerializer(MyModelSerializer, SupplierReturnableMixin, ItemsReturnableMixin):
  supplier = s.SerializerMethodField()
  supplier_id__name = s.SerializerMethodField()
  items__name = s.SerializerMethodField()
  date = s.DateTimeField(format="%A, %d %B %Y %I:%M%p")

  class Meta:
    model = PurchaseOrder
    fields = '__all__'

    
class ReceivingReportSerializer(MyModelSerializer, SupplierReturnableMixin, ItemsReturnableMixin):
  supplier = s.SerializerMethodField()
  supplier_id__name = s.SerializerMethodField()
  items__name = s.SerializerMethodField()
  date = s.DateTimeField(format="%A, %d %B %Y %I:%M%p")

  class Meta:
    model = ReceivingReport
    fields = '__all__'

    
class PaymentReceiptSerializer(MyModelSerializer):
  date = s.DateTimeField(format="%A, %d %B %Y %I:%M%p")

  class Meta:
    model = PaymentReceipt
    fields = '__all__'

    
class SupplierSerializer(MyModelSerializer):
  class Meta:
    model = Supplier
    fields = '__all__'

    
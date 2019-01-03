from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import Context, Template, loader
from arfi.models import *
# from
import pydf
import requests
import json
import re

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def get_protocol(request):
  if request.is_secure():
    return "https://"
  else:
    return "http://"

def get_data(model):
  return (convert(model._meta.object_name) + "s", model._meta.verbose_name.title())


NAVBAR_DATA = [
  ('Revenue Cycle',
    [
      # get_data(Client),
      # get_data(Mandor),
      get_data(ServiceOrder),
      get_data(JobOrder),
      get_data(ServiceBill),
      get_data(BudgetPlan),
    ]
  ),
  ('Expenditure Cycle',
    [
      get_data(PurchaseOrder),
      get_data(ReceivingReport),
      get_data(PaymentReceipt),
    ]
  ),
  ('Inventory',
    [
      get_data(Item),
    ]
  )
]

# Create your views here.
def index(request):
  return render(request, 'arfi/index.html', {
    'navbar': NAVBAR_DATA
  })


def clients_view(request):
  return render(request, 'arfi/tables/clients_table.html', {
    'navbar': NAVBAR_DATA,
    'title': 'Client',
  })

# Revenue
def service_orders_view(request):
  return render(request, 'arfi/tables/service_orders_table.html', {
    'navbar': NAVBAR_DATA,
    'title': 'Service Order',
  })

def job_orders_view(request):
  return render(request, 'arfi/tables/job_orders_table.html', {
    'navbar': NAVBAR_DATA,
    'title': 'Job Order',
  })

def service_bills_view(request):
  return render(request, 'arfi/tables/service_bills_table.html', {
    'navbar': NAVBAR_DATA,
    'title': 'Service Bill',
  })

def budget_plans_view(request):
  return render(request, 'arfi/tables/budget_plans_table.html', {
    'navbar': NAVBAR_DATA,
    'title': 'Budget Plan',
  })

# Expenditure
def purchase_orders_view(request):
  return render(request, 'arfi/tables/purchase_orders_table.html', {
    'navbar': NAVBAR_DATA,
    'title': 'Purchase Order',
  })

def items_view(request):
  return render(request, 'arfi/tables/items_table.html', {
    'navbar': NAVBAR_DATA,
    'title': 'Inventory List',
  })

def receiving_reports_view(request):
  return render(request, 'arfi/tables/receiving_reports_table.html', {
    'navbar': NAVBAR_DATA,
    'title': 'Receiving Report',
  })

def payment_receipts_view(request):
  return render(request, 'arfi/tables/payment_receipts_table.html', {
    'navbar': NAVBAR_DATA,
    'title': 'Payment Receipt',
  })

# pdf
def service_bills_pdf(request, id):
  sb = ServiceBill.objects.filter(id=id)
  print(sb)

  options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
  }

  rendered = render(request, 'arfi/receipt.html', {
    'invoice_id': id
  })
  raw_html = rendered.content.decode('UTF-8')
  pdf = pydf.generate_pdf(raw_html, page_size="A4")
  # return rendered
  return HttpResponse(pdf, content_type='application/pdf')

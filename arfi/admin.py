from django.contrib import admin

from arfi.models import *

admin.site.register(Client)
admin.site.register(Mandor)
admin.site.register(JobOrder)
admin.site.register(ServiceOrder)
admin.site.register(ServiceBill)
admin.site.register(BudgetPlan)
admin.site.register(Transaction)
admin.site.register(PurchaseOrder)
admin.site.register(Item)
admin.site.register(ReceivingReport)
admin.site.register(PaymentReceipt)
admin.site.register(Supplier)
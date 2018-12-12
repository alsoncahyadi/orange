from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

from arfi.models import *

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('Admin | Jasa Teknik Elektrik')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('JASA TEKNIK ELEKTRIK')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Operation Administration Site')

admin_site = MyAdminSite()

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

admin_site.register(Client)
admin_site.register(Mandor)
admin_site.register(JobOrder)
admin_site.register(ServiceOrder)
admin_site.register(ServiceBill)
admin_site.register(BudgetPlan)
admin_site.register(Transaction)
admin_site.register(PurchaseOrder)
admin_site.register(Item)
admin_site.register(ReceivingReport)
admin_site.register(PaymentReceipt)
admin_site.register(Supplier)
from django.db import models as m

# Create your models here.
# Revenue
class Client(m.Model):
  class Meta:
    verbose_name = "Client"
    verbose_name_plural = "Clients"
  
  def __str__(self):
    return "{}: {} (ID: {})".format(self.__class__.__name__, self.name, self.id)

  id = m.AutoField(verbose_name="Client ID", primary_key=True)
  name = m.CharField(max_length=200, verbose_name="Nama Client", db_index=True)
  address = m.CharField(max_length=500, verbose_name="Alamat", db_index=True)


class Mandor(m.Model):
  class Meta:
    verbose_name = "Mandor"
    verbose_name_plural = "Mandor-Mandor"
  
  def __str__(self):
    return "{}: {} (ID: {})".format(self.__class__.__name__, self.name, self.id)

  id = m.AutoField(verbose_name="Mandor ID", primary_key=True)
  name = m.CharField(max_length=200, verbose_name="Nama Mandor", db_index=True)
  address = m.CharField(max_length=500, verbose_name="Alamat", db_index=True)
  phone = m.CharField(max_length=20, verbose_name="No. HP", db_index=True)


class JobOrder(m.Model):
  class Meta:   
    verbose_name = "Job Order"
    verbose_name_plural = "Job Orders"

  id = m.AutoField(verbose_name="No.Order", primary_key=True)
  date = m.DateTimeField(verbose_name="Tanggal", db_index=True)
  mandor_id = m.ForeignKey(Mandor, verbose_name="Mandor ID", on_delete=m.DO_NOTHING)
  # mandor_name
  job_info = m.CharField(max_length=1000, verbose_name="Uraian Pekerjaan")


class ServiceOrder(m.Model):
  class Meta:
    verbose_name = "Service Order"
    verbose_name_plural = "Service Orders"

  id = m.AutoField(verbose_name="No.Order", primary_key=True)
  date = m.DateTimeField(verbose_name="Tanggal", db_index=True)
  client_id = m.ForeignKey(Client, verbose_name="Client ID", on_delete=m.DO_NOTHING)
  # client_name
  project_name = m.CharField(max_length=200, verbose_name="Nama Proyek", db_index=True)
  address = m.CharField(max_length=500, verbose_name="Alamat", db_index=True)
  jobs = m.ManyToManyField(JobOrder, verbose_name="List Pekerjaan")


class ServiceBill(m.Model):
  class Meta:
    verbose_name = "Service Bill"
    verbose_name_plural = "Service Bills"

  id = m.AutoField(verbose_name="No.Order", primary_key=True)
  service_order_id = m.OneToOneField(ServiceOrder, verbose_name="Service Order ID", on_delete=m.DO_NOTHING, db_index=True)
  date = m.DateTimeField(verbose_name="Tanggal", db_index=True)
  client_id = m.ForeignKey(Client, verbose_name="Client ID", on_delete=m.DO_NOTHING, default=None)
  # client_name
  project_name = m.CharField(max_length=200, verbose_name="Nama Proyek", db_index=True)
  address = m.CharField(max_length=500, verbose_name="Alamat", db_index=True)
  jobs = m.ManyToManyField(JobOrder, verbose_name="List Pekerjaan")
  price = m.BigIntegerField(verbose_name="Harga")
  total_price = m.BigIntegerField(verbose_name="Total Harga")


class BudgetPlan(m.Model):
  class Meta:
    verbose_name = "Rencana Anggaran Biaya"
    verbose_name_plural = "Rencana Anggaran Biaya"

  id = m.AutoField(verbose_name="No.Order", primary_key=True)
  service_order_id = m.OneToOneField(ServiceOrder, verbose_name="Service Order ID", on_delete=m.DO_NOTHING, db_index=True)
  job_info = m.CharField(max_length=1000, verbose_name="Uraian Pekerjaan", db_index=True)
  volume = m.CharField(max_length=200, db_index=True)
  unit = m.CharField(max_length=20, db_index=True)
  price = m.BigIntegerField(verbose_name="Harga")
  amount = m.BigIntegerField(verbose_name="Jumlah")
  # total

# Expenditure
class Transaction(m.Model):
  class Meta:
    verbose_name = "Transaction"
    verbose_name_plural = "Transactions"

  def __str__(self):
    return "{}: {} {} (ID: {})".format(self.__class__.__name__, self.item, self.quantity, self.id)

  purchase_order = m.ForeignKey('PurchaseOrder', verbose_name="Purchase Order", on_delete=m.DO_NOTHING)
  item = m.ForeignKey('Item', verbose_name="Item", on_delete=m.DO_NOTHING)
  receiving_report = m.ForeignKey('ReceivingReport', verbose_name="Receiving Report", on_delete=m.DO_NOTHING)
  quantity = m.BigIntegerField(verbose_name="Quantity", default=1)
  created_at = m.DateTimeField(auto_now_add=True, db_index=True)
  updated_at = m.DateTimeField(auto_now=True, db_index=True)


class Item(m.Model):
  class Meta:
    verbose_name = "Inventory List"
    verbose_name_plural = "Inventory Lists"

  def __str__(self):
    return "{}: {} (ID: {})".format(self.__class__.__name__, self.name, self.id)
  
  updated_at = m.DateTimeField(verbose_name="Tanggal Diperbaharui", auto_now=True, db_index=True)
  name = m.CharField(verbose_name="Nama Barang", max_length=200, default="", db_index=True)
  quantity = m.BigIntegerField(verbose_name="Quantity", default=0)
  price = m.BigIntegerField(verbose_name="Harga", default=0)


class PurchaseOrder(m.Model):
  class Meta:
    verbose_name = "Purchase Order"
    verbose_name_plural = "Purchase Orders"

  id = m.AutoField(verbose_name="PO. Number", primary_key=True)
  date = m.DateTimeField(verbose_name="Tanggal", db_index=True)
  supplier_id = m.ForeignKey('Supplier', verbose_name="Supplier ID", on_delete=m.DO_NOTHING)
  # supplier_name
  # item_number, item_name
  items = m.ManyToManyField(Item, verbose_name="Items list", through=Transaction)


class ReceivingReport(m.Model):
  class Meta:
    verbose_name = "Receiving Report"
    verbose_name_plural = "Receiving Reports"

  purchase_order = m.OneToOneField(PurchaseOrder, verbose_name="Purchase Order ID", on_delete=m.DO_NOTHING, null=True, db_index=True)
  supplier_id = m.ForeignKey('Supplier', verbose_name="Supplier ID", on_delete=m.DO_NOTHING)
  # supplier_name
  date = m.DateTimeField(verbose_name="Tanggal", db_index=True)
  items = m.ManyToManyField(Item, verbose_name="Items list", through=Transaction)


class PaymentReceipt(m.Model):
  class Meta:
    verbose_name = "Payment Receipt"
    verbose_name_plural = "Payment Receipts"

  purchase_order = m.OneToOneField(PurchaseOrder, verbose_name="Purchase Order ID", on_delete=m.DO_NOTHING, null=True, db_index=True)
  date = m.DateTimeField(verbose_name="Tanggal", db_index=True)
  bill = m.BigIntegerField(verbose_name="Tagihan")
  total = m.BigIntegerField(verbose_name="Total")
  confirmation = m.CharField(max_length=200, db_index=True)


class Supplier(m.Model):
  class Meta:
    verbose_name = "Supplier"
    verbose_name_plural = "Suppliers"

  def __str__(self):
    return "{}: {} (ID: {})".format(self.__class__.__name__, self.name, self.id)

  name = m.CharField(max_length=200, verbose_name="Nama Supplier", db_index=True)
  address = m.CharField(verbose_name="Alamat", max_length=200, db_index=True)
  phone = m.CharField(max_length=20, verbose_name="No. HP", db_index=True)
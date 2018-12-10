from django.db import models as m

# Create your models here.

class Client(m.Model):
  class Meta:
    verbose_name = "Client"
    verbose_name_plural = "Clients"

  id = m.AutoField(verbose_name="Client ID", primary_key=True)
  name = m.CharField(max_length=200, verbose_name="Nama Client")
  address = m.CharField(max_length=500, verbose_name="Alamat")


class Mandor(m.Model):
  verbose_name = "Client"
  id = m.AutoField(verbose_name="Mandor ID", primary_key=True)
  name = m.CharField(max_length=200, verbose_name="Nama Mandor")
  address = m.CharField(max_length=500, verbose_name="Alamat")
  phone = m.CharField(max_length=20, verbose_name="No. HP")


class JobOrder(m.Model):
  id = m.AutoField(verbose_name="No.Order", primary_key=True)
  date = m.DateTimeField(verbose_name="Tanggal", )
  mandor_id = m.ForeignKey(Mandor, verbose_name="Mandor ID", on_delete=m.DO_NOTHING)
  mandor_name = m.CharField(max_length=200, verbose_name="Nama Mandor")
  job_info = m.CharField(max_length=1000, verbose_name="Uraian Pekerjaan")


class ServiceOrder(m.Model):
  id = m.AutoField(verbose_name="No.Order", primary_key=True)
  date = m.DateTimeField(verbose_name="Tanggal")
  client_id = m.ForeignKey(Client, verbose_name="Client ID", on_delete=m.DO_NOTHING)
  client_name = m.CharField(max_length=200, verbose_name="Nama Client")
  project_name = m.CharField(max_length=200, verbose_name="Nama Proyek")
  address = m.CharField(max_length=500, verbose_name="Alamat")
  jobs = m.ManyToManyField(JobOrder, verbose_name="List Pekerjaan")


class ServiceBill(m.Model):
  id = m.AutoField(verbose_name="No.Order", primary_key=True)
  service_order_id = m.OneToOneField(ServiceOrder, verbose_name="Service Order ID", on_delete=m.DO_NOTHING, db_index=True)
  date = m.DateTimeField(verbose_name="Tanggal")
  client_name = m.CharField(max_length=200, verbose_name="Nama Client")
  project_name = m.CharField(max_length=200, verbose_name="Nama Proyek")
  address = m.CharField(max_length=500, verbose_name="Alamat")
  jobs = m.ManyToManyField(JobOrder, verbose_name="List Pekerjaan")
  price = m.BigIntegerField(verbose_name="Harga")
  total_price = m.BigIntegerField(verbose_name="Total Harga")


class BudgetPlan(m.Model):
  id = m.AutoField(verbose_name="No.Order", primary_key=True)
  service_order_id = m.OneToOneField(ServiceOrder, verbose_name="Service Order ID", on_delete=m.DO_NOTHING, db_index=True)
  job_info = m.CharField(max_length=1000, verbose_name="Uraian Pekerjaan")
  volume = m.CharField(max_length=200)
  unit = m.CharField(max_length=20)
  price = m.BigIntegerField(verbose_name="Harga")
  amount = m.BigIntegerField(verbose_name="Jumlah")
  # total


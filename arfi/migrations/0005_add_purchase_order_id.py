# Generated by Django 2.1.4 on 2018-12-12 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arfi', '0004_remove_servicebill_client_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentreceipt',
            name='purchase_order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='arfi.PurchaseOrder', verbose_name='Purchase Order ID'),
        ),
        migrations.AddField(
            model_name='receivingreport',
            name='purchase_order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='arfi.PurchaseOrder', verbose_name='Purchase Order ID'),
        ),
        migrations.AlterField(
            model_name='receivingreport',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nama Supplier'),
        ),
    ]

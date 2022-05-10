# Generated by Django 3.2.11 on 2022-05-08 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_defalutshippinginfo_defaultbillinginfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='billinginfo',
            name='use_defalut_address',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='shippinginfo',
            name='use_deflt_address',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

# Generated by Django 3.2.11 on 2022-05-20 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0078_auto_20220519_0628'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimg',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterModelOptions(
            name='woocommerceproductlist',
            options={'ordering': ['pk']},
        ),
    ]

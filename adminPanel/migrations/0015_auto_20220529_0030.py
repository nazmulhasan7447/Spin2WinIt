# Generated by Django 3.2.11 on 2022-05-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0014_membershiprank'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershiprank',
            name='number_of_prodct_need_to_sell',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='membershiprank',
            name='total_earnings',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]

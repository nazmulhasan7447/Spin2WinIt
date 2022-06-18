# Generated by Django 3.2.11 on 2022-06-15 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_rename_spent_amount_creditwallet_total_credts_ofcurrentuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='winningchance',
            name='total_spin_tokens_of_crnt_usr',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='winningchance',
            name='purchased',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='winningchance',
            name='remaining_chances',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='winningchance',
            name='spent',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

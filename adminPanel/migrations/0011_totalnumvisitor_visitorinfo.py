# Generated by Django 3.2.11 on 2022-05-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0010_customermessagelist'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalNumVisitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_visitor', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='VisitorInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_ip', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]

# Generated by Django 4.2.8 on 2023-12-25 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
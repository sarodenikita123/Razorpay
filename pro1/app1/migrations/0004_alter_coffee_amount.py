# Generated by Django 5.0.6 on 2024-05-11 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_coffee_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='amount',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]

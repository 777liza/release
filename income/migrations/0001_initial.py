# Generated by Django 5.0.7 on 2024-08-04 15:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_income', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('base_income', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('base_income_description', models.CharField(max_length=100)),
                ('base_income_start_date', models.DateField(blank=True, null=True)),
                ('base_income_end_date', models.DateField(blank=True, null=True)),
                ('investment_income', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('additional_incomes', models.JSONField(blank=True, null=True)),
                ('one_time_incomes', models.JSONField(blank=True, null=True)),
                ('update_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

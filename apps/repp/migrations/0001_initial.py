# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginreg', '0006_auto_20160825_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=100)),
                ('routing_number', models.BigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bank_Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repp.Bank')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginreg.User')),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum', models.DecimalField(decimal_places=2, max_digits=19)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=50)),
                ('card_type', models.CharField(max_length=50)),
                ('card_number', models.BigIntegerField()),
                ('exp_date', models.DateField()),
                ('card_code', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginreg.User')),
            ],
        ),
        migrations.CreateModel(
            name='Lender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lend_amount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('min_payment_date', models.DateField()),
                ('payment_deadline', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_name', models.CharField(max_length=50)),
                ('descrption', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='lender',
            name='loan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repp.Loan'),
        ),
        migrations.AddField(
            model_name='lender',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginreg.User'),
        ),
        migrations.AddField(
            model_name='borrower',
            name='loan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repp.Loan'),
        ),
        migrations.AddField(
            model_name='borrower',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginreg.User'),
        ),
    ]

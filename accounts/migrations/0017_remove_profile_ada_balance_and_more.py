# Generated by Django 4.2.6 on 2024-03-29 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_trade_lost_trade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ada_balance',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bnb_balance',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='doge_balance',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sol_balance',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='usdc_balance',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='xlm_balance',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='xrp_balance',
        ),
    ]

# Generated by Django 3.1 on 2021-01-14 01:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wallet', '0004_withdraw_approved'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Withdraw',
            new_name='WithdrawRequest',
        ),
        migrations.AddField(
            model_name='wallet',
            name='amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='FundWallet',
        ),
    ]

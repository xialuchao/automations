# Generated by Django 2.0.2 on 2019-07-05 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0002_caseinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='caseinfo',
            name='caseAddress',
            field=models.CharField(default='abc', max_length=1024, verbose_name='用例接口地址'),
        ),
    ]

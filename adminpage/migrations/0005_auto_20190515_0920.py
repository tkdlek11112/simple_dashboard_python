# Generated by Django 2.2 on 2019-05-15 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0004_auto_20190514_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='faq_id',
            field=models.TextField(default='0000000000000001', max_length=16),
        ),
        migrations.AlterField(
            model_name='faq',
            name='faq_type',
            field=models.TextField(default='999', max_length=10),
        ),
    ]

# Generated by Django 2.2 on 2019-05-15 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0005_auto_20190515_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='faq_id',
            field=models.CharField(default='0000000000000001', max_length=16),
        ),
        migrations.AlterField(
            model_name='faq',
            name='faq_type',
            field=models.CharField(default='999', max_length=10),
        ),
    ]

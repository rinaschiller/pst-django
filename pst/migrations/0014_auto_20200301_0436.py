# Generated by Django 2.1.4 on 2020-03-01 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pst', '0013_auto_20200301_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='flirtation',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='identity_attack',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='sexually_explicit',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='toxicity',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
    ]

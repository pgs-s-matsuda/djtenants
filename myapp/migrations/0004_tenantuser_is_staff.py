# Generated by Django 3.2.3 on 2021-06-22 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_add_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenantuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='isStaff'),
        ),
    ]

# Generated by Django 3.2.3 on 2021-06-22 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_setup_data'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.RunSQL(
            """
            Insert into django_site (domain, name) values ('localhost','localhost')
            """,
            reverse_sql="""
            delete from django_site where domain='localhost'
            """
        ),
    ]

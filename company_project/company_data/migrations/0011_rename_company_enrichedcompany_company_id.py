# Generated by Django 5.1 on 2024-08-15 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_data', '0010_rename_company_id_enrichedcompany_company_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrichedcompany',
            old_name='company',
            new_name='company_id',
        ),
    ]
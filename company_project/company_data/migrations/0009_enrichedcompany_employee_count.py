# Generated by Django 5.1 on 2024-08-15 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_data', '0008_rename_companyid_enrichedcompany_company_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrichedcompany',
            name='employee_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
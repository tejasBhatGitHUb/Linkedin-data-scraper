# Generated by Django 5.1 on 2024-08-15 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_data', '0009_enrichedcompany_employee_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrichedcompany',
            old_name='company_id',
            new_name='company',
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

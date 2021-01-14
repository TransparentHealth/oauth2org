# Generated by Django 2.2.10 on 2020-08-27 13:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patientface_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crosswalk',
            name='issuer',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='crosswalk',
            name='fhir_patient_id',
            field=models.CharField(blank=True, db_index=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='crosswalk',
            name='fhir_source',
            field=models.TextField(blank=True, default='https://nwt-staging.azurehealthcareapis.com/'),
        ),
        migrations.AlterField(
            model_name='crosswalk',
            name='user_identifier',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='crosswalk',
            unique_together={('user', 'user_identifier', 'issuer')},
        ),
    ]
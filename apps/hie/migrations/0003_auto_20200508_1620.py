# Generated by Django 2.2.10 on 2020-05-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hie', '0002_auto_20190827_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='hieprofile',
            name='activate_staged_user_response',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='hieprofile',
            name='activate_staged_user_response_code',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='hieprofile',
            name='cda2fhir_response',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='hieprofile',
            name='cda2fhir_response_code',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='hieprofile',
            name='consumer_directive_response',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='hieprofile',
            name='consumer_directive_response_code',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='hieprofile',
            name='get_cda_response',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='hieprofile',
            name='get_cda_response_code',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='hieprofile',
            name='patient_search_response',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='hieprofile',
            name='patient_search_response_code',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='hieprofile',
            name='fhir_content_embellish',
            field=models.TextField(blank=True, default='', help_text='Reserved for future use.'),
        ),
    ]

# Generated by Django 2.1.2 on 2019-04-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hixny', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hixnyprofile',
            name='step_1',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='hixnyprofile',
            name='step_2',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='hixnyprofile',
            name='step_3',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='hixnyprofile',
            name='step_4',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='hixnyprofile',
            name='step_5',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='hixnyprofile',
            name='terms_accepted',
            field=models.TextField(blank=True, default=''),
        ),
    ]

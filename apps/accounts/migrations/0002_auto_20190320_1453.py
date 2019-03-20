# Generated by Django 2.1.2 on 2019-03-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='sex',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('', 'Unknown')], default='', help_text='Birth Sex Gender', max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender_identity',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('TMF', 'Transgender Male to Female'), ('TFM', 'Transgender Female to Male'), ('U', 'Unknown')], default='U', help_text='Gender Identity', max_length=3),
        ),
    ]
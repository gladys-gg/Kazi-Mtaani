# Generated by Django 3.2.2 on 2022-06-23 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kazimtaani', '0003_alter_job_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='job',
            unique_together=set(),
        ),
    ]

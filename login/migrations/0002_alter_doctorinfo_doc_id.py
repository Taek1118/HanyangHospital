# Generated by Django 4.2.6 on 2023-11-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorinfo',
            name='doc_id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]

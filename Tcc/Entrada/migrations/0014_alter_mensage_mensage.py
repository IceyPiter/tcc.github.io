# Generated by Django 4.2.5 on 2023-10-23 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entrada', '0013_alter_mensage_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensage',
            name='mensage',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
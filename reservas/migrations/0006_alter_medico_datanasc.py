# Generated by Django 4.1.7 on 2023-06-09 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0005_especialidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='datanasc',
            field=models.DateField(blank=True, null=True),
        ),
    ]
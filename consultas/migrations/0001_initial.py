# Generated by Django 4.2.1 on 2023-06-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('crm', models.CharField(max_length=20)),
                ('data', models.DateTimeField()),
                ('horario', models.CharField(max_length=20)),
            ],
        ),
    ]

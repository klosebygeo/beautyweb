# Generated by Django 4.2.1 on 2023-05-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(max_length=650)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('tip_produs', models.CharField(choices=[('1', 'Ingrijire par'), ('2', 'Ingrijire barba'), ('3', 'Accesorii')], max_length=20)),
                ('um', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]

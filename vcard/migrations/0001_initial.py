# Generated by Django 4.2.7 on 2023-11-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.CharField(max_length=50, unique=True)),
                ('DisplayName', models.CharField(max_length=200)),
                ('Company', models.CharField(max_length=200)),
                ('Position', models.CharField(max_length=200)),
                ('PhoneNumber', models.CharField(max_length=12)),
                ('Address', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=50)),
                ('Website', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserQRLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.CharField(max_length=50)),
                ('QRPath', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.CharField(max_length=50, unique=True)),
                ('UserName', models.CharField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=15)),
            ],
        ),
    ]
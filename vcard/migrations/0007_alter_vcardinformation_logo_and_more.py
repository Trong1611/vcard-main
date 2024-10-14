# Generated by Django 4.2.7 on 2024-09-27 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0006_vcardinformation_logo_vcardinformation_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vcardinformation',
            name='logo',
            field=models.CharField(db_column='logo', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='vcardinformation',
            name='template',
            field=models.IntegerField(db_column='template', default=0),
        ),
    ]

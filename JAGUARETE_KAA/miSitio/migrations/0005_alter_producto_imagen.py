# Generated by Django 3.2.5 on 2021-07-06 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miSitio', '0004_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
    ]
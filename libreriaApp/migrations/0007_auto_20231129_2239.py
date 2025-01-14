# Generated by Django 3.0.14 on 2023-11-30 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreriaApp', '0006_auto_20231129_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreriaApp.autor'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]

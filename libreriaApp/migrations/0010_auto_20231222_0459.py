# Generated by Django 3.0.14 on 2023-12-22 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreriaApp', '0009_auto_20231130_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreriaApp.autor'),
        ),
    ]
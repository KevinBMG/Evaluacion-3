# Generated by Django 3.0.14 on 2023-12-22 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreriaApp', '0012_auto_20231222_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreriaApp.autor'),
        ),
    ]

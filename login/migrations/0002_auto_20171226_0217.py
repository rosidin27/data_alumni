# Generated by Django 2.0 on 2017-12-25 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahasiswa',
            name='verif',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'NO')], default='N', max_length=1),
        ),
    ]
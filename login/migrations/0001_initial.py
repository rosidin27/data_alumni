# Generated by Django 2.0 on 2017-12-25 19:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('username', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('npm', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=128)),
                ('jk', models.CharField(choices=[('P', 'Perempuan'), ('L', 'Laki-laki')], max_length=1)),
                ('prodi', models.CharField(choices=[('mi', 'D3 Manajemen Informatika'), ('ilkom', 'S1 Ilmu Komputer')], max_length=20)),
                ('no_telp', models.CharField(max_length=15)),
                ('alamat', models.TextField(blank=True)),
                ('angkatan', models.CharField(max_length=4)),
                ('tahun_lulus', models.CharField(max_length=4)),
                ('poto', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('verif', models.CharField(choices=[('Y', 'Yes'), ('N', 'NO')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pekerjaan',
            fields=[
                ('id_pekerjaan', models.AutoField(primary_key=True, serialize=False)),
                ('nama_pekerjaan', models.CharField(max_length=64)),
                ('deskripsi_pekerjaan', models.TextField(blank=True)),
                ('tahun_mulai', models.CharField(max_length=4)),
                ('tahun_akhir', models.CharField(max_length=4)),
                ('penghasilan', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999999999)])),
                ('mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Mahasiswa')),
            ],
        ),
    ]

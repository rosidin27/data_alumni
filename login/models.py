from django.db import models
# from django.core.validators import MaxValueValidator
# import os
# #import hashlib

# # Create your models here.

# class Admin(models.Model):
# 	username = models.CharField(primary_key=True, max_length=64)
# 	nama = models.CharField(max_length=64)
# 	password = models.CharField(max_length=32)

# 	def login(cek):
# 		mhs_login = list(Admin.objects.values().filter(username=cek['username'],password=cek['password']))
# 		return mhs_login

# 	def update_password(data):
# 		d = {'error':'', 'success':False}
# 		try:
# 			adm = Admin.objects.filter(username=data['username']).update(password = data['password'])
# 			d['success'] = True
# 		except Exception as e:
# 			d['error'] = str(e)
# 		return d

# class Mahasiswa(models.Model):
# 	CHOICE_PRODI = (('mi','D3 Manajemen Informatika'),('ilkom','S1 Ilmu Komputer'))
# 	CHOICE_JK = (('P','Perempuan'),('L','Laki-laki'))
# 	CHOICE_VERIF = (('Y','Yes'),('N','NO'))

# 	npm = models.CharField(primary_key=True, max_length=10)
# 	nama = models.CharField(max_length=64)
# 	email = models.CharField(max_length=128)
# 	tgl_lahir = models.DateField(blank=False, default="1900-01-01")
# 	jk = models.CharField(max_length=1, choices=CHOICE_JK)
# 	prodi = models.CharField(max_length=20, choices=CHOICE_PRODI)
# 	no_telp = models.CharField(max_length=15)
# 	alamat = models.TextField(blank=True)
# 	angkatan = models.CharField(max_length=4)
# 	tahun_lulus = models.CharField(max_length=4)
# 	poto = models.ImageField(upload_to = 'static/img/foto/', default = 'static/img/foto/no-img.jpg')
# 	password = models.CharField(max_length=32)
# 	verif = models.CharField(max_length=1, choices=CHOICE_VERIF, default=CHOICE_VERIF[1][0])

# 	def hapus(primary_key):
# 		data = {'error':'', 'success':False}
# 		try:
# 			mhs = Mahasiswa.objects.filter(npm=primary_key)
# 			mhs.delete()
# 			data['success'] = True
# 			return data
# 		except Exception as e:
# 			data['error'] = str(e)
# 			return data

# 	def verifData(update):
# 		data = {'error':'', 'success':False}
# 		try:
# 			mhs = Mahasiswa.objects.filter(npm=update['primary_key']).update(verif=update['status'])
# 			data['success'] = True
# 			return data
# 		except Exception as e:
# 			data['error'] = str(e)
# 			return data

# 	def getData(prodi):
# 		if prodi == "all":
# 			mhsList = list(Mahasiswa.objects.values().order_by('verif').reverse())
# 		elif prodi == "mi":
# 			mhsList = list(Mahasiswa.objects.values().filter(prodi='mi').order_by('verif').reverse())
# 		elif prodi == "ilkom":
# 			mhsList = list(Mahasiswa.objects.values().filter(prodi='ilkom').order_by('verif').reverse())
# 		else:
# 			mhsList = list(Mahasiswa.objects.values().order_by('verif').reverse())

# 		return mhsList

# 	def login(cek):
# 		mhs_login = list(Mahasiswa.objects.values().filter(npm=cek['npm'],password=cek['password'],verif=cek['verif']))
# 		return mhs_login

# 	def update(data):
# 		d = {'error':'', 'success':False}
# 		try:
# 			mhs = Mahasiswa.objects.filter(npm=data['npm'])
# 			mhs.update(
# 				nama = data['nama'],
# 				email = data['email'],
# 				tgl_lahir = data['tgl_lahir'],
# 				jk = data['jk'],
# 				prodi = data['prodi'],
# 				no_telp = data['no_telp'],
# 				alamat = data['alamat'],
# 				angkatan = data['angkatan'],
# 				tahun_lulus = data['tahun_lulus']
# 			)

# 			if 'password' in data.keys():
# 				mhs.update(password = data['password'])
# 			if 'poto' in data.keys():
# 				try:
# 				    os.remove(data['delete'])
# 				except Exception as e:
# 				    d['error'] = str(e)
# 				m = Mahasiswa.objects.get(npm=data['npm'])
# 				m.poto =  data['poto']
# 				m.save()

# 			#mhs.save()
# 			#mhs.save(update_fields=fields)
# 			d['success'] = True
# 		except Exception as e:
# 			d['error'] = str(e)

# 		return d

# 	def input(data):
# 		d = {'error':'', 'success':False}
# 		try:
# 			mhs = Mahasiswa.objects.create(
# 				npm=data['npm'],
# 				nama = data['nama'],
# 				email = data['email'],
# 				tgl_lahir = data['tgl_lahir'],
# 				jk = data['jk'],
# 				prodi = data['prodi'],
# 				no_telp = data['no_telp'],
# 				alamat = data['alamat'],
# 				angkatan = data['angkatan'],
# 				tahun_lulus = data['tahun_lulus'],
# 				password = data['password'],
# 				poto = data['poto'],
# 				verif = "N"
# 			)
# 			d['success'] = True
# 		except Exception as e:
# 			d['error'] = str(e)

# 		return d

# class Pekerjaan(models.Model):
# 	id_pekerjaan = models.AutoField(primary_key=True)
# 	mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
# 	nama_pekerjaan = models.CharField(max_length=64)
# 	deskripsi_pekerjaan = models.TextField(blank=True)
# 	tahun_mulai = models.CharField(max_length=4)
# 	tahun_akhir = models.CharField(max_length=4)
# 	penghasilan = models.PositiveIntegerField(validators=[MaxValueValidator(99999999999)])


# # p1 = hashlib.md5("admin".encode('utf-8')).hexdigest()
# # p2 = hashlib.md5(p1.encode('utf-8')).hexdigest()
# # entry = Admin(username='admin', nama='Muhamamd Rosidin', password=p2)
# # entry.save()


# 		
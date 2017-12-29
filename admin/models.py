from django.core.validators import MaxValueValidator
from django.db import models
import os

# Create your models here.
class Admin(models.Model):
	username = models.CharField(primary_key=True, max_length=64)
	nama = models.CharField(max_length=64)
	password = models.CharField(max_length=32)

	def login(cek):
		mhs_login = list(Admin.objects.values().filter(username=cek['username'],password=cek['password']))
		return mhs_login

	def update_password(data):
		d = {'error':'', 'success':False}
		try:
			adm = Admin.objects.filter(username=data['username']).update(password = data['password'])
			d['success'] = True
		except Exception as e:
			d['error'] = str(e)
		return d
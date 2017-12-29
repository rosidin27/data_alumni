from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from login import models as model_login
from admin import models as model_admin
from alumni import models as model_mhs
from datetime import datetime
import hashlib

class NameForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)

def index(request):
	# if 'username' in request.session:
	# 	del request.session['username']
	# View code here...
	y = list()
	year = int(datetime.now().year)
	for i in range((int(datetime.now().year) - 22),year+1,1):
		y.append(i)

	if 'username' not in request.session:
		if request.method == 'POST':
			if request.POST.get('registrasi') == "registrasi":
				if request.POST.get('pass1') == request.POST.get('pass2'):
					paswd = request.POST.get('pass1')
					p1 = hashlib.md5(paswd.encode('utf-8')).hexdigest()
					password = (hashlib.md5(p1.encode('utf-8')).hexdigest())
					
					reg_status = registrasi(request,password)
					if(reg_status['success'] == True):
						return HttpResponse("<script>alert('Registrasi Sukses !!!, Perlu diketahui bahwa, setiap alumni yang mendaftar pada sistem ini harus melalui proses verifikasi, setelah data terverifikasi anda dapat melakukan login');window.location='"+base_url(request)+"/login/'</script>")
					else:
						error = reg_status['error']
						return HttpResponse("<script>alert("+error+");history.back();</script>")
				else:
					return HttpResponse("<script>alert('Password Tidak Sama !');history.back();</script>")
			else:
				form = NameForm(request.POST)
				if form.is_valid():
					username = request.POST.get('username', '')
					p1 = hashlib.md5(request.POST.get('password','').encode('utf-8')).hexdigest()
					password = (hashlib.md5(p1.encode('utf-8')).hexdigest())

					#cek data mahasiswa
					dataMhs = model_mhs.Mahasiswa.login({'npm':username,'password':password,'verif':"Y"})
					if(len(dataMhs) > 0):
						request.session['username'] = username
						request.session['level'] = "alumni"

						return HttpResponse("<script>window.location='"+base_url(request)+"/alumni/?prodi=all'</script>")
					else:
						#cek data admin
						dataAdmin = model_admin.Admin.login({'username':username,'password':password})
						if(len(dataAdmin) > 0):
							mhs = list(model_mhs.Mahasiswa.objects.values().filter(npm=username,verif='Y'))
							request.session['username'] = username
							request.session['level'] = "admin"

							return HttpResponse("<script>window.location='"+base_url(request)+"/admin/?prodi=all'</script>")
						else:
							return HttpResponse("<script>alert('Username atau password salah !');window.location='"+base_url(request)+"/login'</script>")
				else:
					return HttpResponse("<script>alert('Username atau password salah !');window.location='"+base_url(request)+"/login'</script>")
		else:
			get = {
				'year':y,
				'HOST':base_url(request)
			}
			return render(request,'login.html',{ 'get': get })
	else:
		if request.session['level'] == "admin":
			return HttpResponse("<script>window.location='"+base_url(request)+"/admin/?prodi=all'</script>")
		else:
			return HttpResponse("<script>window.location='"+base_url(request)+"/alumni/?prodi=all'</script>")

def logout(request):
	if 'username' not in request.session:
		return HttpResponse("<script>window.location='"+base_url(request)+"/login'</script>")
	else:
		request.session.flush()
		return HttpResponse("<script>window.location='"+base_url(request)+"/login'</script>")

def base_url(request):
	return "http://"+str(request.META['HTTP_HOST'])
#request.get_full_path()

def registrasi(request,password):
	d = {
		'npm' : request.POST.get('npm'),
		'nama' : request.POST.get('nama'),
		'email' : request.POST.get('email'),
		'tgl_lahir' : request.POST.get('tgl_lahir'),
		'jk' : request.POST.get('jk'),
		'prodi' : request.POST.get('prodi'),
		'no_telp' : request.POST.get('no_telp'),
		'alamat' : request.POST.get('alamat'),
		'angkatan' : request.POST.get('angkatan'),
		'tahun_lulus' : request.POST.get('tahun_lulus'),
		'password' : password,
		'poto' : request.FILES.get('foto'),
		'biografi' : request.POST.get('biografi')
	}

	reg_status = model_mhs.Mahasiswa.input(d)

	return reg_status
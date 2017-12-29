from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.db import models
from login import models as model_login
from admin import models as model_admin
from alumni import models as model_mhs
from datetime import datetime
import hashlib
# Create your views here.

def index(request):
	# if 'username' in request.session:
	#  	del request.session['username']
	#  	return HttpResponse("Logout")

	if request.session.keys():
		if request.session['level'] != "alumni":
			return HttpResponse("<script>window.location='"+base_url(request)+"/login'</script>")
		else:
			getProdi =  request.GET.get('prodi','all')
			mhsList = model_mhs.Mahasiswa.getData(getProdi,request.session['level'])
			#return HttpResponse(getProdi)

			session = getSession(request)
			get = {
				'HOST':base_url(request),
				'session':session, 
				'mhsList': mhsList, 
				'action':'list',
				'title':getTitle(getProdi),
				'label':getProdi
			}
			return render(request, 'alumni_index.html', {'get':get})
		#return HttpResponse(session)
	else:
		return HttpResponse("<script>window.location='"+base_url(request)+"/login'</script>")

def view(request):
	get_npm = request.GET.get('npm',False)
	if request.session.keys() and get_npm != False:
		if request.session['level'] != "alumni":
			return HttpResponse("<script>window.location='"+base_url(request)+"/login'</script>")
		else:
			mhs = list(model_mhs.Mahasiswa.objects.values().filter(npm=get_npm,verif='Y'))
			#return HttpResponse(mhs)
			if len(mhs) <= 0:
				return HttpResponse("<script>alert('Data Tidak Ditemukan !');window.location='"+base_url(request)+"/"+request.session['level']+"/?prodi=all'</script>")
			else:
				mhs[0]['tgl_lahir'] = datetime.strptime(str(mhs[0]['tgl_lahir']), '%Y-%m-%d').strftime('%d %B %Y')
				y = list()
				year = int(datetime.now().year)
				for i in range((int(datetime.now().year) - 22),year+1,1):
					y.append(str(i))
				session = getSession(request)
				get = {
					'label':'all', 
					'title':'VIEW DATA ALUMNI',
					'HOST':base_url(request),
					'session':session,
					'action':'view',
					'year':tuple(y),
					'mhs':mhs[0]
				}
				return render(request, 'alumni_index.html', {'get':get})
	else:
		return HttpResponse("<script>alert('Data Tidak Ditemukan !');window.location='"+base_url(request)+"/"+request.session['level']+"/?prodi=all'</script>")


def base_url(request):
	return "http://"+str(request.META['HTTP_HOST'])

def getSession(request):
	session = {"level": request.session['level'], "username": request.session['username']}
	if session['level'] == "admin":
		user = list(model_admin.Admin.objects.values('nama','username','password').filter(username=session['username']))
	elif session['level'] == "alumni":
		user = list(model_mhs.Mahasiswa.objects.values('nama','npm','poto').filter(npm=session['username']))

	session['nama_user'] = user[0]['nama']
	session['poto'] = user[0]['poto']

	return session

def getTitle(prodi):
	if prodi == "all":
		return "SEMUA DATA ALUMNI"
	elif prodi == "mi":
		return "DATA ALUMNI PRODI D3 MANAJEMEN INFORMATIKA"
	elif prodi == "ilkom":
		return "DATA ALUMNI PRODI S1 ILMU KOMPUTER"
	else:
		return "SEMUA DATA ALUMNI"

def password(request):
	if request.session.keys():
		if request.session['level'] != "alumni":
			return HttpResponse("<script>window.location='"+base_url(request)+"/login'</script>")
		else:
			session = getSession(request)
			get = {
				'label':'no_label', 
				'title':'EDIT DATA PASSWORD',
				'HOST':base_url(request),
				'session':session,
				'action':'password'
			}
			if request.method == 'POST':
				if request.POST.get('pass1') == request.POST.get('pass2'):
					
					old_pass1 = hashlib.md5(request.POST.get('pass').encode('utf-8')).hexdigest()
					old_pass2 = hashlib.md5(old_pass1.encode('utf-8')).hexdigest()

					paswd = request.POST.get('pass1')
					p1 = hashlib.md5(paswd.encode('utf-8')).hexdigest()
					password = (hashlib.md5(p1.encode('utf-8')).hexdigest())

					check_password = list(model_mhs.Mahasiswa.objects.values().filter(npm=session['username'],password=old_pass2))
					if(len(check_password) > 0):
						d = {
							'username' : session['username'],
							'password' : password
						}
						update_status = model_mhs.Mahasiswa.update_password(d)
						if(update_status['success'] == True):
							return HttpResponse("<script>alert('Data Tersimpan !');window.location='"+base_url(request)+"/"+session['level']+"/?prodi=all'</script>")
						else:
							return HttpResponse("Error : "+update_status['error']+"<br>"+str(d))
					else:
						return HttpResponse("<script>alert('Password tidak valid !');history.back();</script>")
				else:
					return HttpResponse("<script>alert('Password tidak sama !');history.back();</script>")
			return render(request, 'index.html', {'get':get})

def profil(request):
	get_npm = request.session['username']
	if request.session.keys() and get_npm != False:
		if request.session['level'] != "alumni":
			return HttpResponse("<script>window.location='"+base_url(request)+"/login'</script>")
		else:
			mhs = list(model_mhs.Mahasiswa.objects.values().filter(npm=get_npm,verif='Y'))
			#return HttpResponse(mhs)
			if len(mhs) <= 0:
				return HttpResponse("<script>alert('Data Tidak Ditemukan !');window.location='"+base_url(request)+"/"+request.session['level']+"/?prodi=all'</script>")
			else:
				mhs[0]['tgl_lahir'] = str(mhs[0]['tgl_lahir'])
				if request.method == 'POST':
					d = dict()
					if request.FILES.get('foto'):
						d = {'poto': request.FILES.get('foto'),'delete':mhs[0]['poto']}

					if request.POST.get('pass1') != "":
						if request.POST.get('pass1') == request.POST.get('pass2'):
							paswd = request.POST.get('pass1')
							p1 = hashlib.md5(paswd.encode('utf-8')).hexdigest()
							password = (hashlib.md5(p1.encode('utf-8')).hexdigest())
							d.update({'password' : password})
						else:
							return HttpResponse("<script>alert('Password tidak sama !');history.back();</script>")

					d.update({
						'npm' : get_npm,
						'nama' : request.POST.get('nama'),
						'email' : request.POST.get('email'),
						'tgl_lahir' : request.POST.get('tgl_lahir'),
						'jk' : request.POST.get('jk'),
						'prodi' : request.POST.get('prodi'),
						'no_telp' : request.POST.get('no_telp'),
						'alamat' : request.POST.get('alamat'),
						'angkatan' : request.POST.get('angkatan'),
						'tahun_lulus' : request.POST.get('tahun_lulus'),
						'biografi' : request.POST.get('biografi')
					})
					input_status = model_mhs.Mahasiswa.update(d)
					if(input_status['success'] == True):
						return HttpResponse("<script>alert('Data Tersimpan !');window.location='"+base_url(request)+"/"+request.session['level']+"/?prodi=all'</script>")
					else:
						return HttpResponse("Error : "+input_status['error']+"<br>"+str(d))
					
				y = list()
				year = int(datetime.now().year)
				for i in range((int(datetime.now().year) - 22),year+1,1):
					y.append(str(i))
				session = getSession(request)
				get = {
					'label':'all', 
					'title':'EDIT DATA PROFIL',
					'HOST':base_url(request),
					'session':session,
					'action':'edit',
					'year':tuple(y),
					'mhs':mhs[0]
				}
				return render(request, 'index.html', {'get':get})
	else:
		return HttpResponse("<script>alert('Data Tidak Ditemukan !');window.location='"+base_url(request)+"/"+request.session['level']+"/?prodi=all'</script>")
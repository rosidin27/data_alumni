from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	if 'username' in request.session:
		if request.session['level'] == "mahasiswa":
			return HttpResponse('Index')
		else:
			return HttpResponse("<script>window.location='/"+request.session['level']+"'</script>")
	else:
		return HttpResponse("<script>window.location='/login'</script>")
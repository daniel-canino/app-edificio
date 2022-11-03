from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
	return render(request,'plazasuite/home.html', {}) 


def fondo_bomba(request):
	if request.method == "POST":
		form = BombaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else: 
		form = BombaForm()

	context = {'form' : form}
	return render(request, 'plazasuite/fondo_bomba.html', context)


def fondo_antena(request):
	if request.method == "POST":
		form = AntenaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')	

	else: 
		form = AntenaForm()

	context = {'form' : form}
	return render(request, 'plazasuite/fondo_antena.html', context)

def fondo_salon(request):
	if request.method == "POST":
		form = SalonForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')		

	else: 
		form = SalonForm()

	context = {'form' : form}
	return render(request, 'plazasuite/fondo_salon.html', context)

def index(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else: 
		form = UserForm()

	context = {'form' : form}
	return render(request, 'plazasuite/index.html', context)	

def pago_mensuales(request):
	if request.method == "POST":
		form = MesPagosForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else: 
		form = MesPagosForm()

	context = {'form' : form}
	return render(request, 'plazasuite/pagos_mensuales.html', context)

def pago_extra(request):
	if request.method == "POST":
		form = ExtraPagosForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else: 
		form = ExtraPagosForm()

	context = {'form' : form}
	return render(request, 'plazasuite/pagos_extraordinarios.html', context)



def ver_bomba(request):
	bombas = Fondo_bomba.objects.all()

	context = {'bombas': bombas}
	return render(request,"plazasuite/ver_bomba.html", context)

def ver_salon(request):
	salones = Fondo_salon.objects.all()

	context = {'salones' : salones}
	return render(request, "plazasuite/ver_salon.html", context)

def ver_antena(request):
	antenas = Fondo_antena.objects.all()

	context = {'antenas' : antenas}
	return render(request, "plazasuite/ver_antena.html", context)

def ver_mes(request):
	meses = Pagos_mensuales.objects.all()

	context = {'meses' : meses}
	return render(request, "plazasuite/ver_mes.html", context)


def ver_extra(request):
	extras = Pagos_extra.objects.all()

	context = {'extras' : extras}
	return render(request, "plazasuite/ver_extra.html", context)


def eliminar_bomba(request, fondo_bomba_id):
	bombas = Fondo_bomba.objects.get(id=fondo_bomba_id)
	bombas.delete()
	return redirect('ver_bomba')


def eliminar_antena(request, fondo_antena_id):
	antenas = Fondo_antena.objects.get(id=fondo_antena_id)
	antenas.delete()
	return redirect('ver_antena')

def eliminar_salon(request, fondo_salon_id):
	salones = Fondo_salon.objects.get(id=fondo_salon_id)
	salones.delete()
	return redirect('ver_salon')

def eliminar_mes(request, mes_id):
	meses = Pagos_mensuales.objects.get(id=mes_id)
	meses.delete()
	return redirect('ver_mes')

def eliminar_extra(request, extra_id):
	extras = Pagos_extra.objects.get(id=extra_id)
	extras.delete()
	return redirect('ver_extra')
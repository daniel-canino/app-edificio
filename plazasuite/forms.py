from django import forms
from .models import *


class BombaForm(forms.ModelForm):

	class Meta:
		model = Fondo_bomba
		fields = ['descripcion','capital', 'fecha', 'detalle', 'informacion']

class SalonForm(forms.ModelForm):

	class Meta:
		model = Fondo_salon
		fields = ['descripcion', 'capital','fecha', 'detalle', 'informacion']

class AntenaForm(forms.ModelForm):

	class Meta:
		model = Fondo_antena
		fields = ['descripcion', 'capital','fecha', 'detalle', 'informacion']

class MesPagosForm(forms.ModelForm):

	class Meta:
		model = Pagos_mensuales
		fields = ['nombre', 'n_apartamento', 'capital', 'fecha', 'mes_pago', 'metodo_pago']

class ExtraPagosForm(forms.ModelForm):

	class Meta:
		model = Pagos_extra
		fields = ['n_apartamento', 'fecha', 'capital', 'detalle', 'informacion']


class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['user']
		
	password = forms.CharField(label="Password", widget=forms.PasswordInput, strip=False)
	
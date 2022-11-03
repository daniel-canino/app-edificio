from django.db import models

class Fondo_salon(models.Model):

	descripcion = models.CharField(max_length=50)
	capital = models.IntegerField()
	fecha = models.DateField()
	informacion = models.CharField(max_length=50)
	detalle = models.CharField(max_length=50)

	def __str__(self):
		return self.descripcion


class Fondo_bomba(models.Model):


	descripcion = models.CharField(max_length=50)
	capital = models.IntegerField()
	fecha = models.DateField()
	informacion = models.CharField(max_length=50)
	detalle = models.CharField(max_length=50)


	def __str__(self):
		return self.descripcion



class Fondo_antena(models.Model):

	descripcion = models.CharField(max_length=50)
	capital = models.IntegerField()
	fecha = models.DateField()
	informacion = models.CharField(max_length=50)
	detalle = models.CharField(max_length=50)

	def __str__(self):
		return self.descripcion

class Pagos_mensuales(models.Model):

	nombre = models.CharField(max_length=20)
	n_apartamento = models.CharField(max_length=10)
	capital = models.IntegerField()
	fecha = models.DateField()
	mes_pago = models.CharField(max_length=10)
	metodo_pago = models.CharField(max_length=15)

	def __str__(self):
		return self.n_apartamento



class Pagos_extra(models.Model):

	n_apartamento = models.CharField(max_length=10)
	fecha = models.DateField()
	capital = models.IntegerField()
	detalle = models.CharField(max_length=50)
	informacion = models.CharField(max_length=50)

	def __str__(self):
		return self.n_apartamento


class User(models.Model):

	user = models.CharField(max_length=10)
	password = models.CharField( max_length=10)

	def __str__(self):
		return self.user
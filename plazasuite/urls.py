from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

 	path("", views.index, name='index'),
 	path("home/", views.home, name="home"),
 	path("fondo_bomba/", views.fondo_bomba, name='fondo_bomba'),
 	path("fondo_salon/", views.fondo_salon, name='fondo_salon'),
 	path("fondo_antena/", views.fondo_antena, name='fondo_antena'),
 	path("ver_bomba/", views.ver_bomba, name='ver_bomba'),
 	path("ver_salon/", views.ver_salon, name='ver_salon'),
 	path("ver_antena/", views.ver_antena, name='ver_antena'),
 	path("pago_mensuales/", views.pago_mensuales, name='pago_mensuales'),
 	path("pago_extra/", views.pago_extra, name='pago_extra'),
 	path("ver_extra/", views.ver_extra, name='ver_extra'),
 	path("ver_mes/", views.ver_mes, name='ver_mes'),
 	path("eliminar_bomba/<int:fondo_bomba_id>/", views.eliminar_bomba, name='eliminar_bomba'),
 	path("eliminar_antena/<int:fondo_antena_id>/", views.eliminar_antena, name='eliminar_antena'),
 	path("eliminar_salon/<int:fondo_salon_id>/", views.eliminar_salon, name='eliminar_salon'),
 	path("eliminar_mes/<int:mes_id>/", views.eliminar_mes, name='eliminar_mes'),
 	path("eliminar_extra/<int:extra_id>/", views.eliminar_extra, name='eliminar_extra'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
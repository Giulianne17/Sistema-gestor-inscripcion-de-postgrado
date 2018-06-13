from django.test import TestCase
from django.forms import ModelForm
from InscripcionPostgrado.models import *
from InscripcionPostgrado.forms import *

# Create your tests here.

# Pruebas de la tabla Profesor
class ProfesorTestCase(TestCase):
	def setUp(self):
		coord = Coordinacion.objects.create(Cod_coordinacion = "EE", Nombre_coordinacion = "Arquitectura")

	def test_profesorCedulaEsquina1(self):
		form_data = {
			'Id_prof' : '00000000',
			'Apellidos' : 'Aular Lopez',
			'Nombres' : 'Luis Jose',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorCedulaEsquina2(self):
		form_data = {
			'Id_prof' : '99999999',
			'Apellidos' : 'Aular Lopez',
			'Nombres' : 'Luis Jose',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorCedulaFrontera1(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'Aular Lopez',
			'Nombres' : 'Luis Jose',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())


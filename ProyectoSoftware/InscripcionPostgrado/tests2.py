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

	def test_profesorNombreEsquina1(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'Aular Lopez',
			'Nombres' : 'AA',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())


	def test_profesorNombreEsquina2(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'Aular Lopez',
			'Nombres' : 'ZZ',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorNombreEsquina3(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'Aular Lopez',
			'Nombres' : 'aa',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorNombreEsquina4(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'Aular Lopez',
			'Nombres' : 'zz',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())


	def test_profesorNombreFrontera1(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'Aular Lopez',
			'Nombres' : 'ALAN',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorNombreFrontera2(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'Aular Lopez',
			'Nombres' : 'ZORO',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorNombreFrontera3(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'Aular Lopez',
			'Nombres' : 'alan',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorNombreFrontera4(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'Aular Lopez',
			'Nombres' : 'zoro',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorNombreFrontera5(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'Aular Lopez',
			'Nombres' : 'Laura Lorena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorApellidosEsquina1(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'AA',
			'Nombres' : 'Luis Jose',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorApellidosEsquina2(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'ZZ',
			'Nombres' : 'Luis Jose',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorApellidosEsquina3(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'aa',
			'Nombres' : 'Luis Jose',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorApellidosEsquina4(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'zz',
			'Nombres' : 'Luis Jose',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorApellidosFrontera1(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'AULAR',
			'Nombres' : 'Luis Jose',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorApellidosFrontera2(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'ZAPATA',
			'Nombres' : 'Luis Jose',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorApellidosFrontera3(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'aular',
			'Nombres' : 'Luis Jose',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorApellidosFrontera4(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'zapata',
			'Nombres' : 'Luis Jose',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_profesorApellidosFrontera5(self):
		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'Rangel Pino',
			'Nombres' : 'Laura Lorena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())
	
	# Casos de prueba malicia para la cedula del profesor.
	
	#Caso donde la cedula contiene el caracter "/".
	def test_profesorCedulaMalicia(self):
		form_data = {
			'Id_prof' : '256/829',
			'Apellidos' : 'Rangel Pino',
			'Nombres' : 'Laura Lorena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		self.assertFalse(form.is_valid())
	
	# Caso donde la cedula contiene el caracter ":".
	def test_profesorCedulaMalicia1(self):
		form_data = {
			'Id_prof' : '25:6829',
			'Apellidos' : 'Rangel Pino',
			'Nombres' : 'Laura Lorena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		self.assertFalse(form.is_valid())
	
	# Caso donde el nombre contiene un "@"
	def test_profesorNombreMalicia(self):
		form_data = {
			'Id_prof' : '256829',
			'Apellidos' : 'Rangel Pino',
			'Nombres' : 'Laura@Lorena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		self.assertFalse(form.is_valid())

	#Caso donde el nombre contiene "["	
	def test_profesorNombreMalicia1(self):
		form_data = {
			'Id_prof' : '256829',
			'Apellidos' : 'Rangel Pino',
			'Nombres' : 'L[auraLorena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		self.assertFalse(form.is_valid())
	
	#Caso donde el nombre contiene "{"	
	def test_profesorNombreMalicia2(self):
		form_data = {
			'Id_prof' : '256829',
			'Apellidos' : 'Rangel Pino',
			'Nombres' : 'Laura Lor{ena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		self.assertFalse(form.is_valid())
	
		# Caso donde el apellido contiene un "@"
	def test_profesorApellidoMalicia(self):
		form_data = {
			'Id_prof' : '256829',
			'Apellidos' : 'Ra@ngel Pino',
			'Nombres' : 'Laura Lorena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		self.assertFalse(form.is_valid())

	#Caso donde el apellido contiene "["	
	def test_profesorApellidoMalicia1(self):
		form_data = {
			'Id_prof' : '256829',
			'Apellidos' : 'R[ngel Pino',
			'Nombres' : 'LauraLorena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		self.assertFalse(form.is_valid())
	
	#Caso donde el apellido contiene "{"	
	def test_profesorApellidoMalicia2(self):
		form_data = {
			'Id_prof' : '256829',
			'Apellidos' : 'Rangel Pi{no',
			'Nombres' : 'Laura Lor{ena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		self.assertFalse(form.is_valid())


# Pruebas de la tabla Ofrece
class OfreceTestCase(TestCase):
	def setUp(self):
		coord = Coordinacion.objects.create(Cod_coordinacion = "EE", Nombre_coordinacion = "Arquitectura")

		form_data = {
			'Cod_asignatura': 'EE-1020',
			'Nombre_asig': 'Estudios generales',
			'Cod_coordinacion': 'EE',
			'Creditos': '4',
			'Programa': 'https://www.youtube.com/watch?v=C6MOKXm8x50'
		}
		form = AsignaturaForm(data = form_data)
		form.save()

		form_data1 = {
			'Id_prof' : '24553623',
			'Apellidos' : 'Aular Lopez',
			'Nombres' : 'Luis Jose',
			'Cod_coordinacion': 'EE'
		}
		form1 = ProfesorForm(data = form_data1)
		form1.save()

	# Caso esquina.
	def test_ofrece_horarioEsquina1(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '1-2',
			'Dia' : 'LUNES',
			'Periodo' : 'EM',
			'Anio': 2018,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_ofrece_horarioEsquina2(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '1-13',
			'Dia' : 'LUNES',
			'Periodo' : 'EM',
			'Anio': 2018,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_ofrece_horarioEsquina3(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '12-13',
			'Dia' : 'LUNES',
			'Periodo' : 'EM',
			'Anio': 2018,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	# Casos frontera.
	def test_ofrece_horarioFrontera1(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '1-5',
			'Dia' : 'LUNES',
			'Periodo' : 'AJ',
			'Anio': 2018,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_ofrece_horarioFrontera2(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '7-13',
			'Dia' : 'LUNES',
			'Periodo' : 'EM',
			'Anio': '2018',
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_ofrece_horarioFrontera3(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '7-8',
			'Dia' : 'LUNES',
			'Periodo' : 'V',
			'Anio': 2018,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_ofrece_horarioFrontera4(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '5-6',
			'Dia' : 'LUNES',
			'Periodo' : 'EM',
			'Anio': 2018,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_ofrece_anioEsquina1(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '5-6',
			'Dia' : 'LUNES',
			'Periodo' : 'SD',
			'Anio': 1970,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_ofrece_anioEsquina2(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '5-6',
			'Dia' : 'LUNES',
			'Periodo' : 'SD',
			'Anio': 2019,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_ofrece_anioFrontera1(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '5-6',
			'Dia' : 'LUNES',
			'Periodo' : 'SD',
			'Anio': 2000,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_ofrece_anioFrontera2(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '5-6',
			'Dia' : 'LUNES',
			'Periodo' : 'SD',
			'Anio': 1990,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_ofrece_anioFrontera3(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '5-6',
			'Dia' : 'LUNES',
			'Periodo' : 'SD',
			'Anio': 2018,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_ofrece_periodoEsquina1(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '5-6',
			'Dia' : 'LUNES',
			'Periodo' : 'SD',
			'Anio': 2018,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_ofrece_periodoEsquina2(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '5-6',
			'Dia' : 'LUNES',
			'Periodo' : 'EM',
			'Anio': 2018,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_ofrece_periodoEsquina3(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '5-6',
			'Dia' : 'LUNES',
			'Periodo' : 'AJ',
			'Anio': 2018,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_ofrece_periodoEsquina4(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '5-6',
			'Dia' : 'LUNES',
			'Periodo' : 'V',
			'Anio': 2018,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())
	
	# Casos de Malicia

	#Caso en el que año es 1969
	def test_ofrece_anioMalicia(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '5-6',
			'Dia' : 'LUNES',
			'Periodo' : 'V',
			'Anio': 1969,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		self.assertFalse(form.is_valid())
	
	#Caso en el que año es 2020
	def test_ofrece_anioMalicia1(self):
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '5-6',
			'Dia' : 'LUNES',
			'Periodo' : 'V',
			'Anio': 2020,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		self.assertFalse(form.is_valid())
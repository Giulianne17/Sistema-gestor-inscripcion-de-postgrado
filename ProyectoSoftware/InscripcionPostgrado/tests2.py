from django.test import TestCase
from django.forms import ModelForm
from InscripcionPostgrado.models import *
from InscripcionPostgrado.forms import *

'''
*************************************************
	CASOS DE PRUEBA PARA LA TABLA DE PROFESOR
*************************************************
'''

class ProfesorTestCase(TestCase):
	
	def setUp(self):
		'''La funcion setUp se encarga de crear una instancia en la tabla de coordinacion 
		   para ser utilizada en todos los casos de prueba que se presentan a continuacion
		   
		   Parametro:
		       self (ProfesorTestCase): instancia sobre la que se evaluan los casos
			   
		   Atributo:
		       coord (Coordinacion): instancia de coordinacion creada'''
		
		coord = Coordinacion.objects.create(Cod_coordinacion = "EE", Nombre_coordinacion = "Arquitectura")


	def test_profesorCedulaEsquina1(self):
		'''Esta prueba es de esquina para el atributo cedula
		   Corresponde a la esquina donde todos los caracteres son "0"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''
		
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
		'''Esta prueba es de esquina para el atributo cedula
		   Corresponde a la esquina donde todos los caracteres son "9"
		   Se espera que la instancia sea creada correctamente
		    
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''
		
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
		'''Esta prueba es de frontera para el atributo cedula
		   Corresponde a la combinacion de caracteres entre "0" y "9"
		   Se espera que la instancia sea creada correctamente
		    
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''

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
		'''Esta prueba es de esquina para el atributo nombre
		   Corresponde a la esquina donde todos los caracteres son "A"
		   Se espera que la instancia sea creada correctamente
		    
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''

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
		'''Esta prueba es de esquina para el atributo nombre
		   Corresponde a la esquina donde todos los caracteres son "Z"
		   Se espera que la instancia sea creada correctamente
		    
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''
		
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
		'''Esta prueba es de esquina para el atributo nombre
		   Corresponde a la esquina donde todos los caracteres son "a"
		   Se espera que la instancia sea creada correctamente

		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''
		
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
		'''Esta prueba es de esquina para el atributo nombre
		   Corresponde a la esquina donde todos los caracteres son "z"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''
		
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
		'''Esta prueba es de frontera para el atributo nombre
		   Corresponde a la combinacion de caracteres entre "A" y "Z"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''
		
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
		'''Esta prueba es de frontera para el atributo nombre
		   Corresponde a la combinacion de caracteres entre "A" y "Z"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''
		
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
		'''Esta prueba es de frontera para el atributo nombre
		   Corresponde a la combinacion de caracteres entre "a" y "z"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''
		
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
		'''Esta prueba es de frontera para el atributo nombre
		   Corresponde a la combinacion de caracteres entre "a" y "z"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''
		
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
		'''Esta prueba es de frontera para el atributo nombre
		   Corresponde a la combinacion de caracteres en mayuscula y minuscula
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''
		
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
		'''Esta prueba es de esquina para el atributo apellido
		   Corresponde a la esquina donde todos los caracteres son "A"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''

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
		'''Esta prueba es de esquina para el atributo apellido
		   Corresponde a la esquina donde todos los caracteres son "Z"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''
		   
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
		'''Esta prueba es de esquina para el atributo apellido
		   Corresponde a la esquina donde todos los caracteres son "a"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''
		   
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
		'''Esta prueba es de esquina para el atributo apellido
		   Corresponde a la esquina donde todos los caracteres son "z"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el casos
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''
		   
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
		'''Esta prueba es de frontera para el atributo apellido
		   Corresponde a la combinacion de caracteres entre "A" y "Z"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''

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
		'''Esta prueba es de frontera para el atributo apellido
		   Corresponde a la combinacion de caracteres entre "A" y "Z"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''

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
		'''Esta prueba es de frontera para el atributo apellido
		   Corresponde a la combinacion de caracteres entre "a" y "z"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''

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
		'''Esta prueba es de frontera para el atributo apellido
		   Corresponde a la combinacion de caracteres entre "a" y "z"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''

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
		'''Esta prueba es de frontera para el atributo apellido
		   Corresponde a la combinacion de caracteres en mayuscula y minuscula
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''

		form_data = {
			'Id_prof' : '2561829',
			'Apellidos' : 'Rangel Pino',
			'Nombres' : 'Laura Lorena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())
	

	def test_profesorCedulaMalicia(self):
		'''Esta prueba es de malicia para el atributo cedula
		   Corresponde al string donde un caracter es "/"
		   Se espera que la instancia no sea creada
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''

		form_data = {
			'Id_prof' : '256/829',
			'Apellidos' : 'Rangel Pino',
			'Nombres' : 'Laura Lorena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		self.assertFalse(form.is_valid())
	
	
	def test_profesorCedulaMalicia1(self):
		'''Esta prueba es de malicia para el atributo cedula
		   Corresponde al string donde un caracter es ":"
		   Se espera que la instancia no sea creada
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''

		form_data = {
			'Id_prof' : '25:6829',
			'Apellidos' : 'Rangel Pino',
			'Nombres' : 'Laura Lorena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		self.assertFalse(form.is_valid())
	

	def test_profesorNombreMalicia(self):
		'''Esta prueba es de malicia para el atributo nombre
		   Corresponde al string donde un caracter es "@"
		   Se espera que la instancia no sea creada
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''

		form_data = {
			'Id_prof' : '256829',
			'Apellidos' : 'Rangel Pino',
			'Nombres' : 'Laura@Lorena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		self.assertFalse(form.is_valid())


	def test_profesorNombreMalicia1(self):
		'''Esta prueba es de malicia para el atributo nombre
		   Corresponde al string donde un caracter es "["
		   Se espera que la instancia no sea creada
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''
	
		form_data = {
			'Id_prof' : '256829',
			'Apellidos' : 'Rangel Pino',
			'Nombres' : 'L[auraLorena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		self.assertFalse(form.is_valid())

	
	def test_profesorNombreMalicia2(self):
		'''Esta prueba es de malicia para el atributo nombre
		   Corresponde al string donde un caracter es "{"
		   Se espera que la instancia no sea creada
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''

		form_data = {
			'Id_prof' : '256829',
			'Apellidos' : 'Rangel Pino',
			'Nombres' : 'Laura Lor{ena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		self.assertFalse(form.is_valid())
	

	def test_profesorApellidoMalicia(self):
		'''Esta prueba es de malicia para el atributo apellido
		   Corresponde al string donde un caracter es "@"
		   Se espera que la instancia no sea creada
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''

		form_data = {
			'Id_prof' : '256829',
			'Apellidos' : 'Ra@ngel Pino',
			'Nombres' : 'Laura Lorena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		self.assertFalse(form.is_valid())


	def test_profesorApellidoMalicia1(self):
		'''Esta prueba es de malicia para el atributo apellido
		   Corresponde al string donde un caracter es "["
		   Se espera que la instancia no sea creada
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''

		form_data = {
			'Id_prof' : '256829',
			'Apellidos' : 'R[ngel Pino',
			'Nombres' : 'LauraLorena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		self.assertFalse(form.is_valid())
	
	
	def test_profesorApellidoMalicia2(self):
		'''Esta prueba es de malicia para el atributo apellido y nombre
		   Corresponde a los strings donde un caracter es "{"
		   Se espera que la instancia no sea creada
		   
		   Parametro:
		       self (ProfesorTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia profesor
			   form : objeto del tipo profesor'''

		form_data = {
			'Id_prof' : '256829',
			'Apellidos' : 'Rangel Pi{no',
			'Nombres' : 'Laura Lor{ena',
			'Cod_coordinacion': 'EE'
		}
		form = ProfesorForm(data = form_data)
		self.assertFalse(form.is_valid())


'''
***************************************************
	CASOS DE PRUEBA PARA LA TABLA DE LAS OFERTAS
***************************************************
'''

class OfreceTestCase(TestCase):
	
	def setUp(self):
		'''La funcion setUp se encarga de crear una instancia en la tabla de coordinacion,
		   una instancia en la tabla asignatura y una instancia en la tabla profesor
		   para ser utilizadas en todos los casos de prueba que se presentan a continuacion
		   
		   Parametros:
		    	self (OfreceTestCase): es la instancia sobre la que se evaluan los casos

		   Atributos:
		    	coord (Coordinacion): instancia de coordinacion creada
				form_data : diccionario con los atributos de la intancia asignatura
				form : objeto del tipo profesor
				form_data1 : diccionario con los atributos de la intancia profesor
				form1 : objeto del tipo profesor'''
		
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

		form_data2 = {
			'Periodo': 'EM',
			'Anio': 2018
		}
		form2 = TrimestreForm(data = form_data2)
		form2.save()


	def test_ofrece_horarioEsquina1(self):
		'''Esta prueba es de esquina para el atributo horario
		   Corresponde a la esquina donde el horario es de la forma "1-2"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (OfreceTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Se_Ofrece
			   form : objeto del tipo Se_Ofrece'''

		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '1-2',
			'Dia' : 'LUNES',
			'Periodo' : 1,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())


	def test_ofrece_horarioEsquina2(self):
		'''Esta prueba es de esquina para el atributo horario
		   Corresponde a la esquina donde el horario es de la forma "1-13"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (OfreceTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Se_Ofrece
			   form : objeto del tipo Se_Ofrece'''

		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '1-2',
			'Dia' : 'LUNES',
			'Periodo' : 1,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())


	def test_ofrece_horarioEsquina3(self):
		'''Esta prueba es de esquina para el atributo horario
		   Corresponde a la esquina donde el horario es de la forma "12-13"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (OfreceTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Se_Ofrece
			   form : objeto del tipo Se_Ofrece'''
		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '1-2',
			'Dia' : 'LUNES',
			'Periodo' : 1,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())


	def test_ofrece_horarioFrontera1(self):
		'''Esta prueba es de frontera para el atributo horario
		   Corresponde a un horario entre "1-2" y "1-13"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (OfreceTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Se_Ofrece
			   form : objeto del tipo Se_Ofrece'''

		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '1-2',
			'Dia' : 'LUNES',
			'Periodo' : 1,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

	def test_ofrece_horarioFrontera2(self):
		'''Esta prueba es de frontera para el atributo horario
		   Corresponde a un horario entre "1-2" y "1-13"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (OfreceTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Se_Ofrece
			   form : objeto del tipo Se_Ofrece'''

		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '1-2',
			'Dia' : 'LUNES',
			'Periodo' : 1,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())


	def test_ofrece_horarioFrontera3(self):
		'''Esta prueba es de frontera para el atributo horario
		   Corresponde a un horario entre "1-2" y "12-13"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (OfreceTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Se_Ofrece
			   form : objeto del tipo Se_Ofrece'''

		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '1-2',
			'Dia' : 'LUNES',
			'Periodo' : 1,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())


	def test_ofrece_horarioFrontera4(self):
		'''Esta prueba es de frontera para el atributo horario
		   Corresponde a un horario entre "1-2" y "12-13"
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (OfreceTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Se_Ofrece
			   form : objeto del tipo Se_Ofrece'''

		form_data = {
			'Id_prof' : '24553623',
			'Cod_asignatura' : 'EE-1020',
			'Horario' : '1-2',
			'Dia' : 'LUNES',
			'Periodo' : 1,
			'Cod_coordinacion': 'EE'
		}
		form = Se_OfreceForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())

class TrimestreTestCase(TestCase):

	''' Para los casos de prueba de la tabla Trimestre no es necesario establecer un SetUp 
		ya que no es necesario que haya una estancia de alguna otra tabla para poder
		inicializar esta, debido a que los campos no poseen referencias a otros campos.
	'''

	def test_trimestre_anioEsquina1(self):
		'''Esta prueba es de esquina para el atributo año
		   Corresponde al año 1970
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (TrimestreTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Trimestre
			   form : objeto del tipo Trimestre'''

		form_data = {
			'Periodo' : 'SD',
			'Anio': 1970
		}
		form = TrimestreForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())


	def test_trimestre_anioEsquina2(self):
		'''Esta prueba es de esquina para el atributo año
		   Corresponde al año 2019
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (TrimestreTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Trimestre
			   form : objeto del tipo Trimestre'''

		form_data = {
			'Periodo' : 'SD',
			'Anio': 2019
		}
		form = TrimestreForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())


	def test_trimestre_anioFrontera1(self):
		'''Esta prueba es de frontera para el atributo año
		   Corresponde a un año entre 1970 y 2019
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (TrimestreTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Trimestre
			   form : objeto del tipo Trimestre'''

		form_data = {
			'Periodo' : 'SD',
			'Anio': 2000
		}
		form = TrimestreForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())


	def test_trimestre_anioFrontera2(self):
		'''Esta prueba es de frontera para el atributo año
		   Corresponde a un año entre 1970 y 2019
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (TrimestreTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Trimestre
			   form : objeto del tipo Trimestre'''

		form_data = {
			'Periodo' : 'SD',
			'Anio': 1990
		}
		form = TrimestreForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())


	def test_trimestre_anioFrontera3(self):
		'''Esta prueba es de frontera para el atributo año
		   Corresponde a un año entre 1970 y 2019
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (TrimestreTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Trimestre
			   form : objeto del tipo Trimestre'''

		form_data = {
			'Periodo' : 'SD',
			'Anio': 2018
		}
		form = TrimestreForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())


	def test_trimestre_periodo1(self):
		'''Esta prueba es de esquina para el atributo periodo
		   Corresponde al periodo Septiembre-Diciembre que se almacena como SD
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (TrimestreTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Trimestre
			   form : objeto del tipo Trimestre'''

		form_data = {
			'Periodo' : 'SD',
			'Anio': 2018
		}
		form = TrimestreForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())


	def test_trimestre_periodo2(self):
		'''Esta prueba es de esquina para el atributo periodo
		   Corresponde al periodo Enero-Marzo que se almacena como EM
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (TrimestreTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Trimestre
			   form : objeto del tipo Trimestre'''

		form_data = {
			'Periodo' : 'EM',
			'Anio': 2018
		}
		form = TrimestreForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())


	def test_trimestre_periodo3(self):
		'''Esta prueba es de esquina para el atributo periodo
		   Corresponde al periodo Abril-Julio que se almacena como AJ
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (TrimestreTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Trimestre
			   form : objeto del tipo Trimestre'''

		form_data = {
			'Periodo' : 'AJ',
			'Anio': 2018
		}
		form = TrimestreForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())


	def test_trimestre_periodo4(self):
		'''Esta prueba es de esquina para el atributo periodo
		   Corresponde al periodo Verano que se almacena como V
		   Se espera que la instancia sea creada correctamente
		   
		   Parametro:
		       self (TrimestreTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Trimestre
			   form : objeto del tipo Trimestre'''

		form_data = {
			'Periodo' : 'V',
			'Anio': 2018
		}
		form = TrimestreForm(data = form_data)
		form.save()
		self.assertTrue(form.is_valid())
	
	
	def test_trimestre_anioMalicia(self):
		'''Esta prueba es de malicia para el atributo año
		   Corresponde al año 1969
		   Se espera que la instancia no sea creada
		   
		   Parametro:
		       self (TrimestreTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Trimestre
			   form : objeto del tipo STrimestre'''

		form_data = {
			'Periodo' : 'V',
			'Anio': 1969
		}
		form = TrimestreForm(data = form_data)
		self.assertFalse(form.is_valid())
	
	
	def test_trimestre_anioMalicia1(self):
		'''Esta prueba es de malicia para el atributo año
		   Corresponde al año 2020
		   Se espera que la instancia no sea creada
		   
		   Parametro:
		       self (OfreceTestCase): es la instancia sobre la que se evalua el caso
			      
		   Atributos:
		       form_data : diccionario con los atributos de la intancia Trimestre
			   form : objeto del tipo Trimestre'''

		form_data = {
			'Periodo' : 'V',
			'Anio': 2020
		}
		form = TrimestreForm(data = form_data)
		self.assertFalse(form.is_valid())


from django.test import TestCase
from django.forms import ModelForm
from InscripcionPostgrado.models import *
from InscripcionPostgrado.forms import *

# Create your tests here.

# Pruebas de la tabla Coordinaciones

class CoordinacionTestCase(TestCase):
    def setUp(self):
        pass

# Caso de prueba para verificar que se añaden bien a la BD las coordinaciones
# Falla si no se ha creado la BD
    
    def test_coordinacion_crear(self):
        form_data = {
            'Cod_coordinacion': "AA", 
            'Nombre_coordinacion': "Arquitectura"
        }
        form = CoordinacionForm(data=form_data)
        form.save()
        coord1 = Coordinacion.objects.get(Cod_coordinacion = "AA")
        self.assertEqual(coord1.Nombre_coordinacion, "Arquitectura")

# Caso de prueba para verificar si se añaden instancias que exceden la longitud 
# maxima del codigo de la coordinacion.

    def test_coordinacion_max_cod(self):
        form_data = {
            'Cod_coordinacion': "ABC", 
            'Nombre_coordinacion': "Arquitectura"
        }   	
        form = CoordinacionForm(data=form_data) 
        self.assertFalse(form.is_valid())

# Caso de prueba para verificar si se añaden instancias que poseen longitud menor 
# a 2 para el codigo de la coordinacion.

    def test_coordinacion_min_cod(self):
        form_data = {
            'Cod_coordinacion': "A", 
            'Nombre_coordinacion': "Arquitectura"
        }       
        form = CoordinacionForm(data=form_data) 
        self.assertFalse(form.is_valid())

# Caso de prueba para verificar si se añaden instancias que exceden la longitud 
# maxima del nombre de la coordinacion.

    def test_coordinacion_max_nombre(self):
        form_data = {
            'Cod_coordinacion': "AA", 
            'Nombre_coordinacion': "ArquitecturaArquitecturaArquitectura"
        }   	
        form = CoordinacionForm(data=form_data) 
        self.assertFalse(form.is_valid())

# Caso de prueba para verificar si se añaden instancias que posean la longitud 
# maxima del nombre de la coordinacion.


    def test_coordinacion_exacto_nombre(self):
        form_data = {
            'Cod_coordinacion': "AA", 
            'Nombre_coordinacion': "ArquitecturaArquitecturaArquit"
        }   	
        form = CoordinacionForm(data=form_data) 
        form.save()
        coord1 = Coordinacion.objects.get(Cod_coordinacion = "AA")
        self.assertEqual(coord1.Nombre_coordinacion, "ArquitecturaArquitecturaArquit")

# Caso de prueba para verificar si se añaden instancias que posean la longitud 
# maxima del codigo de la coordinacion.


    def test_coordinacion_exacto_cod(self):
        form_data = {
            'Cod_coordinacion': "AA", 
            'Nombre_coordinacion': "Arquitectura"
        }   	
        form = CoordinacionForm(data=form_data) 
        form.save()
        coord1 = Coordinacion.objects.get(Cod_coordinacion = "AA")
        self.assertEqual(coord1.Nombre_coordinacion, "Arquitectura")        


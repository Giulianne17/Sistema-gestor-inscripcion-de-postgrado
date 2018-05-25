from django.test import TestCase
from django.forms import ModelForm
from InscripcionPostgrado.models import *
from InscripcionPostgrado.forms import *

# Create your tests here.

# Pruebas de la tabla Coordinaciones
# Caso de prueba para verificar que se añaden bien a la BD las coordinaciones
class CoordinacionTestCase(TestCase):
    def setUp(self):
        pass
    
    def test_coordinacion_crear(self):
        form_data = {
            'Cod_coordinacion': "4", 
            'Nombre_coordinacion': "Arquitectura"
        }
        form = CoordinacionForm(data=form_data)
        form.save()
        coord1 = Coordinacion.objects.get(Cod_coordinacion = 4)
        self.assertEqual(coord1.Nombre_coordinacion, "Arquitectura")

# Pruebas de la tabla Asignatura
class AsignaturaTestCase(TestCase):
    def setUp(self):
        coord = Coordinacion.objects.create(Cod_coordinacion = "4", Nombre_coordinacion = "Arquitectura")

    # Verificar que se añade una asignatura
    def test_asignatura_crear(self):
        form_data = {
            'Cod_asignatura': 'EE-102',
            'Nombre_asig': 'Estudios generales',
            'Cod_coordinacion': '4',
            'Creditos': '4'
        }
        form = AsignaturaForm(data = form_data)
        form.save()
        asig = Asignatura.objects.get(Nombre_asig = "Estudios generales")
        self.assertEqual(asig.Cod_asignatura, "EE-102")

    # Verificar que no se añade asignatura con una cantidad de creditos mayores a 30
    def test_asignatura_maxcredit(self):
        form_data = {
            'Cod_asignatura': 'EE-105',
            'Nombre_asig': 'Estudios Generales',
            'Cod_coordinacion': '4',
            'Creditos': '50'
        }
        form = AsignaturaForm(data=form_data)
        self.assertFalse(form.is_valid())

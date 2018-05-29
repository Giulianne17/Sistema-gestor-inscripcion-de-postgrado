from django.test import TestCase
from django.forms import ModelForm
from InscripcionPostgrado.models import *
from InscripcionPostgrado.forms import *

# Create your tests here.

# Pruebas de la tabla Coordinaciones
# Caso de prueba para verificar que se añaden bien a la BD las coordinaciones
class AsignaturaTestCase(TestCase):
    def setUp(self):
        coord = Coordinacion.objects.create(Cod_coordinacion = "EE", Nombre_coordinacion = "Arquitectura")

    # Verificar que se añade una asignatura
    def test_asignatura_crear(self):
        form_data = {
            'Cod_asignatura': 'EE1020',
            'Nombre_asig': 'Estudios generales',
            'Cod_coordinacion': 'EE',
            'Creditos': '4'
        }
        form = AsignaturaForm(data = form_data)
        form.save()
        asig = Asignatura.objects.get(Nombre_asig = "Estudios generales")
        self.assertEqual(asig.Cod_asignatura, 'EE1020')

    # Verificar que se busca una asignatura
    def test_asignatura_consulta(self):

        form_data = {
            'Cod_asignatura': 'MA1111',
            'Nombre_asig': 'Matematicas I',
            'Cod_coordinacion': 'EE',
            'Creditos': '4'
        }
        form = AsignaturaForm(data = form_data)
        form.save()
        asig = Asignatura.objects.filter(Nombre_asig = "Matematicas I")
        self.assertEqual(asig[0].Cod_asignatura, 'MA1111')

    # Verificar que se elimina una asignatura
    def test_asignatura_eliminar(self):
        form_data = {
            'Cod_asignatura': 'EE1020',
            'Nombre_asig': 'Estudios generales',
            'Cod_coordinacion': 'EE',
            'Creditos': '4'
        }
        form = AsignaturaForm(data = form_data)
        form.save()
        asig = Asignatura.objects.get(Nombre_asig = "Estudios generales").delete()
        try:
            asig1 = Asignatura.objects.get(Nombre_asig = "Estudios generales")
        except:
            pass
    # Verificar que no se añade asignatura con una cantidad de creditos mayores a 30

    def test_asignatura_maxcredit(self):
        form_data = {
            'Cod_asignatura': 'EE1050',
            'Nombre_asig': 'Estudios Generales',
            'Cod_coordinacion': 'EE',
            'Creditos': '50'
        }
        form = AsignaturaForm(data=form_data)
        self.assertFalse(form.is_valid())

    # Verificar que no se añade asignatura con longitud mayor a 30 en el nombre

    def test_asignatura_maxnombre(self):
        form_data = {
            'Cod_asignatura': 'EE1050',
            'Nombre_asig': 'Estudios GeneralesEstudios Generales',
            'Cod_coordinacion': 'EE',
            'Creditos': '3'
        }
        form = AsignaturaForm(data=form_data)
        self.assertFalse(form.is_valid())

    # Verificar que no se añade asignatura con longitud mayor a 6 en el codigo

    def test_asignatura_maxcod(self):
        form_data = {
            'Cod_asignatura': 'EE00555',
            'Nombre_asig': 'Estudios Generales',
            'Cod_coordinacion': 'EE',
            'Creditos': '3'
        }
        form = AsignaturaForm(data=form_data)
        self.assertFalse(form.is_valid())

    # Verificar que no se añade asignatura con longitud menor a 6 en el codigo

    def test_asignatura_mincod(self):
        form_data = {
            'Cod_asignatura': 'EE005',
            'Nombre_asig': 'Estudios Generales',
            'Cod_coordinacion': 'EE',
            'Creditos': '3'
        }
        form = AsignaturaForm(data=form_data)
        self.assertFalse(form.is_valid())

    # Verificar que se añade una asignatura con la longitud maxima para el nombre

    def test_asignatura_exactnombre(self):
        form_data = {
            'Cod_asignatura': 'EE0050',
            'Nombre_asig': 'Estudios GeneralesEstudios Gen',
            'Cod_coordinacion': 'EE',
            'Creditos': '3'
        }
        form = AsignaturaForm(data=form_data)
        form.save()
        asig1 = Asignatura.objects.get(Nombre_asig = 'Estudios GeneralesEstudios Gen')
        self.assertEqual(asig1.Cod_asignatura, 'EE0050')

    # Verificar que se añade una asignatura con la longitud maxima para el codigo

    def test_asignatura_exactcod(self):
        form_data = {
            'Cod_asignatura': 'EE1050',
            'Nombre_asig': 'Estudios Generales',
            'Cod_coordinacion': 'EE',
            'Creditos': '3'
        }
        form = AsignaturaForm(data=form_data)
        form.save()
        asig1 = Asignatura.objects.get(Nombre_asig = 'Estudios Generales')
        self.assertEqual(asig1.Cod_asignatura, 'EE1050')

    # Verificar que se añade una asignatura con la cantidad maxima para los creditos

    def test_asignatura_exactcred(self):
        form_data = {
            'Cod_asignatura': 'EE1050',
            'Nombre_asig': 'Estudios Generales',
            'Cod_coordinacion': 'EE',
            'Creditos': '30'
        }
        form = AsignaturaForm(data=form_data)
        form.save()
        asig1 = Asignatura.objects.get(Nombre_asig = 'Estudios Generales')
        self.assertEqual(asig1.Cod_asignatura, 'EE1050')



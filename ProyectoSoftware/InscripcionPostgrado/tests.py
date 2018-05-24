from django.test import TestCase

# Create your tests here.
from InscripcionPostgrado.models import Coordinacion

class CoordinacionTestCase(TestCase):
    def setUp(self):
        Coordinacion.objects.create(Cod_coordinacion = 3, Nombre_coordinacion = "Computacion")
        Coordinacion.objects.create(Cod_coordinacion = 4, Nombre_coordinacion = "Arquitectura")
    
    def test_coordinacion_crear(self):
        coord1 = Coordinacion.objects.get(Cod_coordinacion = 3)
        coord2 = Coordinacion.objects.get(Nombre_coordinacion = "Arquitectura")
        self.assertEqual(coord1.Nombre_coordinacion, "Computacion")
        self.assertEqual(coord2.Cod_coordinacion, str(4))

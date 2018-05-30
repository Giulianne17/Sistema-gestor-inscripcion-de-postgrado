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

    # Verificar que se elimina una coordinacion

    def test_coordinacion_eliminar(self):
        form_data = {
            'Cod_coordinacion': "AA", 
            'Nombre_coordinacion': "Arquitectura"
        }
        form = CoordinacionForm(data = form_data)
        form.save()
        coord1 = Coordinacion.objects.get(Nombre_coordinacion = "Arquitectura").delete()
        try:
            coord1 = Coordinacion.objects.get(Nombre_coordinacion = "Arquitectura")
        except:
            pass

# Caso de prueba para verificar si se añaden instancias que exceden la longitud 
# maxima del codigo de la coordinacion.

    def test_coordinacion_max_cod(self):
        form_data = {
            'Cod_coordinacion': "ABC", 
            'Nombre_coordinacion': "Arquitectura"
        }   	
        form = CoordinacionForm(data=form_data) 
        self.assertFalse(form.is_valid())

# Caso de prueba para verificar si se añaden instancias en las que el codigo de 
# la coordinacion son dos letras minusculas

    def test_coordinacion_minusculas(self):
        form_data = {
            'Cod_coordinacion': "aa", 
            'Nombre_coordinacion': "Arquitectura"
        }       
        form = CoordinacionForm(data=form_data) 
        self.assertFalse(form.is_valid())

# Caso de prueba para verificar si se añaden instancias en las que el codigo de 
# la coordinacion es una letra minuscula

    def test_coordinacion_una_minuscula(self):
        form_data = {
            'Cod_coordinacion': "a", 
            'Nombre_coordinacion': "Arquitectura"
        }       
        form = CoordinacionForm(data=form_data) 
        self.assertFalse(form.is_valid())

# Caso de prueba para verificar si se añaden instancias en las que el codigo de 
# la coordinacion son tres letras minusculas

    def test_coordinacion_max_minusculas(self):
        form_data = {
            'Cod_coordinacion': "aaa", 
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

# Caso de prueba para verificar si se añaden instancias que poseen numeros en
# el codigo de la coordinacion.

    def test_coordinacion_num_cod(self):
        form_data = {
            'Cod_coordinacion': "4", 
            'Nombre_coordinacion': "Arquitectura"
        }       
        form = CoordinacionForm(data=form_data) 
        self.assertFalse(form.is_valid())

# Caso de prueba para verificar si se añaden instancias que poseen numeros en
# el nombre de la coordinacion.

    def test_coordinacion_num_nombre(self):
        form_data = {
            'Cod_coordinacion': "AA", 
            'Nombre_coordinacion': "Arquitectura333"
        }       
        form = CoordinacionForm(data=form_data) 
        #form.save()
        #print(Coordinacion.objects.get(Nombre_coordinacion='Arquitectura333'))
        self.assertFalse(form.is_valid())

# Caso de prueba para verificar si se añaden instancias que poseen espacios en
# el nombre de la coordinacion.

    def test_coordinacion_espacio_nombre(self):
        form_data = {
            'Cod_coordinacion': "CI", 
            'Nombre_coordinacion': "Coordinacion de Computacion"
        }       
        form = CoordinacionForm(data=form_data) 
        self.assertTrue(form.is_valid())

# Caso de prueba para verificar si se añaden instancias que poseen strings vacios en
# el nombre de la coordinacion.

    def test_coordinacion_vacio_nombre(self):
        form_data = {
            'Cod_coordinacion': "CI", 
            'Nombre_coordinacion': ""
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

# Caso de prueba para verificar si se añaden instancias cuya longitud del nombre  
# de la asignatura es menor al maximo.

    def test_coordinacion_min_nombre(self):
        form_data = {
            'Cod_coordinacion': "AA", 
            'Nombre_coordinacion': "Arquitectura"
        }       
        form = CoordinacionForm(data=form_data) 
        form.save()
        coord1 = Coordinacion.objects.get(Cod_coordinacion = "AA")
        self.assertEqual(coord1.Nombre_coordinacion, "Arquitectura")

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

    # Verificar si no se añade una asignatura cuyo codigo tiene caracteres especiales

    def test_asignatura_crear_especial(self):
        form_data = {
            'Cod_asignatura': 'EE-020',
            'Nombre_asig': 'Estudios generales',
            'Cod_coordinacion': 'EE',
            'Creditos': '4'
        }
        form = AsignaturaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # Verificar si no se añade una asignatura cuya cantidad de creditos son caracteres

    def test_asignatura_crear_cred_letras(self):
        form_data = {
            'Cod_asignatura': 'EE1020',
            'Nombre_asig': 'Estudios generales',
            'Cod_coordinacion': 'EE',
            'Creditos': 'aa'
        }
        form = AsignaturaForm(data = form_data)
        self.assertFalse(form.is_valid())


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

    # Verificar que no se añade asignatura con cantidad de letras menor a 2 en el codigo
    # y mas de 4 digitos

    def test_asignatura_una_letra(self):
        form_data = {
            'Cod_asignatura': 'E00005',
            'Nombre_asig': 'Estudios Generales',
            'Cod_coordinacion': 'EE',
            'Creditos': '3'
        }
        form = AsignaturaForm(data=form_data)
        self.assertFalse(form.is_valid())    

    # Verificar que no se añade asignatura con cantidad de letras mayor a 2 en el codigo
    # y menos de 4 digitos

    def test_asignatura_tres_letra(self):
        form_data = {
            'Cod_asignatura': 'EEE005',
            'Nombre_asig': 'Estudios Generales',
            'Cod_coordinacion': 'EE',
            'Creditos': '3'
        }
        form = AsignaturaForm(data=form_data)
        self.assertFalse(form.is_valid())

    # Verificar que no se añade asignatura con letras de codigo minusculas 

    def test_asignatura_letra_minuscula(self):
        form_data = {
            'Cod_asignatura': 'ee0005',
            'Nombre_asig': 'Estudios Generales',
            'Cod_coordinacion': 'EE',
            'Creditos': '3'
        }
        form = AsignaturaForm(data=form_data)
        self.assertFalse(form.is_valid())

    # Verificar que se añade asignatura cuyo nombre es un string vacio

    def test_asignatura_nombre_vacio(self):
        form_data = {
            'Cod_asignatura': 'EE1020',
            'Nombre_asig': '',
            'Cod_coordinacion': 'EE',
            'Creditos': '4'
        }
        form = AsignaturaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # Verificar que se añade asignatura cuyo nombre tiene una longitud menor a 30

    def test_asignatura_num_nombre(self):
        form_data = {
            'Cod_asignatura': 'EE1020',
            'Nombre_asig': 'Estudios generales33',
            'Cod_coordinacion': 'EE',
            'Creditos': '4'
        }
        form = AsignaturaForm(data = form_data)
        self.assertFalse(form.is_valid())

    # Verificar que se añade asignatura cuyo nombre tiene una longitud menor a 30

    def test_asignatura_minnombre(self):
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

    # Verificar que se añade una asignatura con la cantidad invalida para los creditos

    def test_asignatura_cero_cred(self):
        form_data = {
            'Cod_asignatura': 'EE1050',
            'Nombre_asig': 'Estudios Generales',
            'Cod_coordinacion': 'EE',
            'Creditos': '0'
        }
        form = AsignaturaForm(data=form_data)
        self.assertFalse(form.is_valid())

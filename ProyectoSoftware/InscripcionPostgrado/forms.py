from django import forms
from django.forms import ModelForm
from InscripcionPostgrado.models import *
from django.core.exceptions import NON_FIELD_ERRORS

""" En el presente archivo se presentan los forms de todas las
tablas en la base de datos. No todos son utilizados para este
proyecto.
"""


class AsignaturaForm(ModelForm):
    """ Form para añadir una instancia a la tabla de asignaturas.
    """
    class Meta:
        model = Asignatura
        fields = ["Cod_asignatura", "Nombre_asig", "Cod_coordinacion", "Creditos", "Visto", "Programa"]
        error_messages = {
            'Cod_asignatura': {
                'unique': ("Error la asignatura ya existe"),
            }
        }

class CoordinacionForm(ModelForm):
    """ Form para añadir una instancia a la tabla de las
    coordinaciones.
    """
    class Meta:
        model = Coordinacion
        fields = ["Cod_coordinacion", "Nombre_coordinacion"]

class ProfesorForm(ModelForm):
    """ Form para añadir una instancia a la tabla de profesor.
    """
    class Meta:
        model = Profesor
        fields = ["Id_prof","Apellidos","Nombres","Cod_coordinacion"]

class PerteneceForm(ModelForm):
    """ Form para añadir una instancia a la tabla de pertenece
    que relaciona un decanato con una coordinacion.
    """
    class Meta:
        model = Pertenece
        fields = ["Nombre_decanato","Cod_coordinacion"]


class DecanatoForm(ModelForm):
    """ Form para añadir una instancia a la tabla de decanato.
    """
    class Meta:
        model = Decanato
        fields = ["Nombre_decanato"]

class EstudianteForm(ModelForm):
    """ Form para añadir una instancia la tabla de estudiante.
    """
    class Meta:
        model = Estudiante
        fields = ["Carnet","Apellidos","Nombres"]

class TrimestreForm(ModelForm):
    """ Form para añadir un trimestre.
    """
    class Meta:
        model = Trimestre
        fields = ["Periodo","Anio"]
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Ya existe una oferta con estos datos",
            }
        }

class CursaForm(ModelForm):
    """ Form para añadir una instancia a la tabla de cursa que
    relaciona un estudiante con una asignatura que cursa,
    ofertada en cierto periodo y año.
    """
    class Meta:
        model = Cursa
        fields = ["Carnet","Cod_asignatura","Periodo","Anio"]

class Se_OfreceForm(ModelForm):
    """ Form para añadir una instancia a la tabla de se_ofrece,
    que relaciona un profesor con un una asignatura que se
    ofrece en cierto período y año, con un horario y día en
    que se imparte la materia.
    """
    class Meta:
        model = Se_Ofrece
        fields = ["Id_prof","Cod_asignatura","Horario","Dia","Periodo", "Cod_coordinacion"]

class MedioPagoForm(ModelForm):
    """ Form para añadir una instancia a la tabla de
    MedioPago.
    """
    class Meta:
        model = MedioPago
        fields = ["Postiza"]

class Paga_ConForm(ModelForm):
    """ Form para añadir una instancia a la tabla de Paga_Con.
    """
    class Meta:
        model = Paga_Con
        fields = ["Precio","Carnet","Postiza","Periodo","Anio"]

class DebitoForm(ModelForm):
    """ Form para añadir una instancia a la tabla de tarjeta
    de Debito.
    """
    class Meta:
        model = Debito
        fields = ["Nro_Cuenta","Nro_Tarjeta","Tipo","Nombre_Banco","Postiza"]


class CreditoForm(ModelForm):
    """ Form para añadir una instancia a la tabla de tarjeta
    de Credito.
    """
    class Meta:
        model = Credito
        fields = ["Nro_Tarjeta","Fecha_Vence","Nombre_Banco","Postiza"]

class TransferenciaForm(ModelForm):
    """ Form para añadir una instancia a la tabla de
    Transferencia de pago.
    """
    class Meta:
        model = Transferencia
        fields = ["Nro_Referencia","Postiza"]

class DepositoForm(ModelForm):
    """ Form para añadir una instancia a la tabla de Deposito
    de pago.
    """
    class Meta:
        model = Deposito
        fields = ["Referencia","Postiza"]
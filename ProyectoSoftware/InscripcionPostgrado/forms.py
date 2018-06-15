from django import forms
from django.forms import ModelForm
from InscripcionPostgrado.models import *

# Form para añadir una instancia a la tabla de asignaturas
class AsignaturaForm(ModelForm):
    class Meta:
        model = Asignatura
        fields = ["Cod_asignatura", "Nombre_asig", "Cod_coordinacion", "Creditos", "Visto", "Programa"]
        error_messages = {
            'Cod_asignatura': {
                'unique': ("Error la asignatura ya existe"),
            }
        }

# Form para añadir una instancia a la tabla de las coordinaciones
class CoordinacionForm(ModelForm):
    class Meta:
        model = Coordinacion
        fields = ["Cod_coordinacion", "Nombre_coordinacion"]

# Form para añadir una instancia a la tabla de profesor
class ProfesorForm(ModelForm):
    class Meta:
        model = Profesor
        fields = ["Id_prof","Apellidos","Nombres","Cod_coordinacion"]

# Form para añadir una instancia a la tabla de pertenece que relaciona un decanato con una coordinacion
class PerteneceForm(ModelForm):
    class Meta:
        model = Pertenece
        fields = ["Nombre_decanato","Cod_coordinacion"]

# Form para añadir una instancia a la tabla de decanato
class DecanatoForm(ModelForm):
    class Meta:
        model = Decanato
        fields = ["Nombre_decanato"]

# Form para añadir una instancia la tabla de estudiante
class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ["Carnet","Apellidos","Nombres"]

# Form para añadir una instancia a la tabla de cursa que relaciona un estudiante con una asignatura que
#cursa, ofertada en cierto periodo y año
class CursaForm(ModelForm):
    class Meta:
        model = Cursa
        fields = ["Carnet","Cod_asignatura","Periodo","Anio"]

# Form para añadir una instancia a la tabla de se_ofrece, que relaciona un profesor con un una asignatura
#que se ofrece en cierto período y año, con un horario y día en que se imparte la materia
class Se_OfreceForm(ModelForm):
    class Meta:
        model = Se_Ofrece
        fields = ["Id_prof","Cod_asignatura","Horario","Dia","Periodo","Anio", "Cod_coordinacion"]

# Form para añadir una instancia a la tabla de MedioPago
class MedioPagoForm(ModelForm):
    class Meta:
        model = MedioPago
        fields = ["Postiza"]

# Form para añadir una instancia a la tabla de Paga_Con
class Paga_ConForm(ModelForm):
    class Meta:
        model = Paga_Con
        fields = ["Precio","Carnet","Postiza","Periodo","Anio"]

# Form para añadir una instancia a la tabla de tarjeta de Debito
class DebitoForm(ModelForm):
    class Meta:
        model = Debito
        fields = ["Nro_Cuenta","Nro_Tarjeta","Tipo","Nombre_Banco","Postiza"]

# Form para añadir una instancia a la tabla de tarjeta de Credito
class CreditoForm(ModelForm):
    class Meta:
        model = Credito
        fields = ["Nro_Tarjeta","Fecha_Vence","Nombre_Banco","Postiza"]

# Form para añadir una instancia a la tabla de Transferencia de pago
class TransferenciaForm(ModelForm):
    class Meta:
        model = Transferencia
        fields = ["Nro_Referencia","Postiza"]

# Form para añadir una instancia a la tabla de Deposito de pago
class DepositoForm(ModelForm):
    class Meta:
        model = Deposito
        fields = ["Referencia","Postiza"]
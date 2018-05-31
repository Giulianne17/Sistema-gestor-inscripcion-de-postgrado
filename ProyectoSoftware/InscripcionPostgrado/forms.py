from django import forms
from django.forms import ModelForm
from InscripcionPostgrado.models import *

# Form para añadir una asignatura
class AsignaturaForm(ModelForm):
    class Meta:
        model = Asignatura
        fields = ["Cod_asignatura", "Nombre_asig", "Cod_coordinacion", "Creditos", "Visto"]
        error_messages = {
            'Cod_asignatura': {
                'unique': ("Error la asignatura ya existe"),
            }
        }

# Form para añadir una coordinacion
class CoordinacionForm(ModelForm):
    class Meta:
        model = Coordinacion
        fields = ["Cod_coordinacion", "Nombre_coordinacion"]

# Form para añadir un profesor
class ProfesorForm(ModelForm):
    class Meta:
        model = Profesor
        fields = ["Id_prof","Apellidos","Nombres","Cod_coordinacion"]

# Form para añadir un pertenece
class PerteneceForm(ModelForm):
    class Meta:
        model = Pertenece
        fields = ["Nombre_decanato","Cod_coordinacion"]

# Form para añadir un decanato
class DecanatoForm(ModelForm):
    class Meta:
        model = Decanato
        fields = ["Nombre_decanato"]

# Form para añadir un estudiante
class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ["Carnet","Apellidos","Nombres"]

# Form para añadir un trimestre
class TrimestreForm(ModelForm):
    class Meta:
        model = Trimestre
        fields = ["Periodo","Anio"]

# Form para añadir un cursa
class CursaForm(ModelForm):
    class Meta:
        model = Cursa
        fields = ["Carnet","Cod_asignatura","Periodo","Anio"]

# Form para añadir un se_ofrece
class Se_OfreceForm(ModelForm):
    class Meta:
        model = Se_Ofrece
        fields = ["Id_prof","Cod_asignatura","Horario","Periodo","Anio", "Cod_coordinacion"]

# Form para añadir un MedioPago
class MedioPagoForm(ModelForm):
    class Meta:
        model = MedioPago
        fields = ["Postiza"]

# Form para añadir un MedioPago
class Paga_ConForm(ModelForm):
    class Meta:
        model = Paga_Con
        fields = ["Precio","Carnet","Postiza","Periodo","Anio"]

# Form para añadir un Debito
class DebitoForm(ModelForm):
    class Meta:
        model = Debito
        fields = ["Nro_Cuenta","Nro_Tarjeta","Tipo","Nombre_Banco","Postiza"]

# Form para añadir un Credito
class CreditoForm(ModelForm):
    class Meta:
        model = Credito
        fields = ["Nro_Tarjeta","Fecha_Vence","Nombre_Banco","Postiza"]

# Form para añadir un Transferencia
class TransferenciaForm(ModelForm):
    class Meta:
        model = Transferencia
        fields = ["Nro_Referencia","Postiza"]

# Form para añadir un Deposito
class DepositoForm(ModelForm):
    class Meta:
        model = Deposito
        fields = ["Referencia","Postiza"]
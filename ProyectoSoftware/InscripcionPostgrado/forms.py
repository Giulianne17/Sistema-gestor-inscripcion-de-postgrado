from django.forms import ModelForm
from InscripcionPostgrado.models import *

# Form para añadir una asignatura
class AsignaturaForm(ModelForm):
    class Meta:
        model = Asignatura
        fields = ['Cod_asignatura', 'Nombre_asig', 'Cod_coordinacion', 'Creditos']

# Form para añadir una coordinacion
class CoordinacionForm(ModelForm):
    class Meta:
        model = Coordinacion
        fields = ['Cod_coordinacion', 'Nombre_coordinacion']

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
from django.db import models

# Create your models here.
class Coordinacion(models.Model):
	Cod_coordinacion = models.CharField(primary_key=True, max_length=3)
	Nombre_coordinacion = models.CharField(max_length=30)
#Duda cuanto es el largo del cod.

class Asignatura(models.Model):
	Cod_asignatura = models.CharField(primary_key=True, max_length=6)
	Nombre_asig = models.CharField(max_length=30)
	Cod_coordinacion = models.ForeignKey(Coordinacion, max_length=3, on_delete=models.CASCADE)
	#creditos = models.DecimalField(max_digits=1, decimal_places=2, default=Decimal(0.00))

class Estudiante(models.Model):
	Carnet = models.CharField(primary_key=True, max_length=8)
	Apellidos = models.CharField(max_length=30)
	Nombres = models.CharField(max_length=30)

class Profesor(models.Model):
	Id_prof = models.CharField(primary_key=True, max_length=7)
	Apellidos = models.CharField(max_length=30)
	Nombres = models.CharField(max_length=30)
	Cod_coordinacion = models.ForeignKey(Coordinacion, max_length=3, on_delete=models.CASCADE)

#Esta generando problemas.
class Trimestre(models.Model):
	Periodo = models.CharField(primary_key=True, max_length=20)
	Anio = models.IntegerField(primary_key=True, max_length=4)

class Pertenece(models.Model):
	Cod_coordinacion = models.ForeignKey(Coordinacion, primary_key=True, on_delete=models.CASCADE)
	Cod_asignatura = models.ForeignKey(Asignatura, primary_key=True, on_delete=models.CASCADE)

'''
	class Meta:
    	unique_together = ('Cod_coordinacion', 'Cod_asignatura',)
'''

class Cursa(models.Model):
	Carnet = models.ForeignKey(Estudiante, primary_key=True, on_delete=models.CASCADE)
	Cod_asignatura = models.ForeignKey(Asignatura, primary_key=True, on_delete=models.CASCADE)
	Periodo = models.ForeignKey(Trimestre, primary_key=True, on_delete=models.CASCADE)
	Anio = models.ForeignKey(Trimestre, primary_key=True, on_delete=models.CASCADE)

class Se_Ofrece(models.Model):
	Id_prof = models.ForeignKey(Profesor, primary_key=True, on_delete=models.CASCADE)
	Cod_asignatura = models.ForeignKey(Asignatura, primary_key=True, on_delete=models.CASCADE)
	Periodo = models.ForeignKey(Trimestre, primary_key=True, on_delete=models.CASCADE)
	Anio = models.ForeignKey(Trimestre, primary_key=True, on_delete=models.CASCADE)

class MedioPago(models.Model):
	Postiza = models.AutoField(primary_key=True)

class Paga_Con(models.Model):
	Carnet = models.ForeignKey(Estudiante, primary_key=True, on_delete=models.CASCADE)
	Postiza = models.ForeignKey(MedioPago, primary_key=True, on_delete=models.CASCADE)
	Periodo = models.ForeignKey(Trimestre, primary_key=True, on_delete=models.CASCADE)
	Anio = models.ForeignKey(Trimestre, primary_key=True, on_delete=models.CASCADE)

class MedioPago(models.Model):
	Postiza = models.AutoField(primary_key=True)

class Debito(models.Model):
	Nro_Cuenta = models.IntegerField(primary_key=True, max_length=20)
	Nro_Tarjeta = models.IntegerField(max_length=18)
	Tipo = models.CharField(max_length=9)
	Nombre_Banco = models.CharField(max_length=30)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)

class Credito(models.Model):
	Nro_Tarjeta = models.IntegerField(primary_key=True,max_length=18)
	Fecha_Vence = models.DateField() 
	Nombre_Banco = models.CharField(max_length=30)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)

class Transferencia(models.Model):
	Nro_Referencia = models.IntegerField(primary_key=True, max_length=20)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)

class Transferencia(models.Model):
	Referencia = models.IntegerField(primary_key=True, max_length=20)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
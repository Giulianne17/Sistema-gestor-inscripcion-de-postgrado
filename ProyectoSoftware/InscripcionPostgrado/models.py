from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Coordinacion(models.Model):
	Cod_coordinacion = models.CharField(primary_key=True, max_length=3)
	Nombre_coordinacion = models.CharField(max_length=30)
#Duda cuanto es el largo del cod.
	def getallfields(self):
		return [self.Cod_coordinacion,self.Nombre_coordinacion]
	def __getallfieldNames__():
		return ["Cod_coordinacion","Nombre_coordinacion"]
	def __gettablename__():
		return "Coordinacion"

class Asignatura(models.Model):
	Cod_asignatura = models.CharField(primary_key=True, max_length=6)
	Nombre_asig = models.CharField(max_length=30)
	Cod_coordinacion = models.ForeignKey(Coordinacion, max_length=3, on_delete=models.CASCADE)
	Creditos = models.IntegerField(validators=[MaxValueValidator(5)])
	def getallfields(self):
		return [self.Cod_asignatura,self.Nombre_asig, self.Cod_coordinacion,self.Creditos]
	def __getallfieldNames__():
		return ["Cod_asignatura","Nombre_asig", "Cod_coordinacion", "creditos"]
	def __gettablename__():
		return "Asignatura"

class Estudiante(models.Model):
	Carnet = models.CharField(primary_key=True, max_length=8)
	Apellidos = models.CharField(max_length=30)
	Nombres = models.CharField(max_length=30)
	def getallfields(self):
		return [self.Carnet,self.Apellidos,self.Nombres]
	def __getallfieldNames__():
		return ["Carnet","Apellidos","Nombres"]
	def __gettablename__():
		return "Estudiante"

class Profesor(models.Model):
	Id_prof = models.CharField(primary_key=True, max_length=7)
	Apellidos = models.CharField(max_length=30)
	Nombres = models.CharField(max_length=30)
	Cod_coordinacion = models.ForeignKey(Coordinacion, max_length=3, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Id_prof,self.Apellidos,self.Nombres,self.Cod_coordinacion]
	def __getallfieldNames__():
		return ["Id_prof","Apellidos","Nombres","Cod_coordinacion"]
	def __gettablename__():
		return "Profesor"

class Trimestre(models.Model):
	class Meta:
		unique_together = (('Periodo', 'Anio'))
	Periodo = models.CharField(max_length=20)
	Anio = models.IntegerField(validators=[MaxValueValidator(9999)])
	def getallfields(self):
		return [self.Periodo,self.Anio]
	def __getallfieldNames__():
		return ["Periodo","Anio"]
	def __gettablename__():
		return "Trimestre"

class Cursa(models.Model):
	class Meta:
		unique_together=(('Carnet', 'Cod_asignatura', 'Periodo', 'Anio'))
	Carnet = models.ForeignKey(Estudiante, primary_key=True, on_delete=models.CASCADE)
	Cod_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
	Periodo = models.ForeignKey(Trimestre, related_name='Trimestre_cursa_periodo', on_delete=models.CASCADE)
	Anio = models.ForeignKey(Trimestre, related_name='Trimestre_cursa_anio', on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Carnet,self.Cod_asignatura,self.Periodo,self.Anio]
	def __getallfieldNames__():
		return ["Carnet","Cod_asignatura","Periodo","Anio"]
	def __gettablename__():
		return "Cursa"

class Se_Ofrece(models.Model):
	class Meta:
		unique_together = (('Id_prof', 'Cod_asignatura','Horario', 'Periodo', 'Anio'))
	Id_prof = models.ForeignKey(Profesor, primary_key=True, on_delete=models.CASCADE)
	Cod_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
	Horario = models.CharField(max_length=5)
	Periodo = models.ForeignKey(Trimestre, related_name='Trimestre_ofrece_periodo', on_delete=models.CASCADE)
	Anio = models.ForeignKey(Trimestre, related_name='Trimestre_ofrece_anio', on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Id_prof,self.Cod_asignatura,self.Horario,self.Periodo,self.Anio]
	def __getallfieldNames__():
		return ["Id_prof","Cod_asignatura","Horario","Periodo","Anio"]
	def __gettablename__():
		return "Se_Ofrece"

class MedioPago(models.Model):
	Postiza = models.AutoField(primary_key=True)
	def getallfields(self):
		return [self.Postiza]
	def __getallfieldNames__():
		return ["Postiza"]
	def __gettablename__():
		return "MedioPago"

class Paga_Con(models.Model):
	class Meta:
		unique_together = (('Carnet', 'Postiza', 'Periodo', 'Anio'))
	Precio = models.DecimalField(max_digits=19, decimal_places=4)
	Carnet = models.ForeignKey(Estudiante, primary_key=True, on_delete=models.CASCADE)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	Periodo = models.ForeignKey(Trimestre, related_name='Trimestre_pago_periodo', on_delete=models.CASCADE)
	Anio = models.ForeignKey(Trimestre, related_name='Trimestre_pago_anio', on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Precio,self.Carnet,self.Cod_asignatura,self.Periodo,self.Anio]
	def __getallfieldNames__():
		return ["Precio","Carnet","Cod_asignatura","Periodo","Anio"]
	def __gettablename__():
		return "Paga_Con"

class Debito(models.Model):
	Nro_Cuenta = models.IntegerField(primary_key=True,validators=[MaxValueValidator(99999999999999999999)])
	Nro_Tarjeta = models.IntegerField(validators=[MaxValueValidator(999999999999999999)])
	Tipo = models.CharField(max_length=9)
	Nombre_Banco = models.CharField(max_length=30)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Nro_Cuenta,self.Nro_Tarjeta,self.Tipo,self.Nombre_Banco,self.Postiza]
	def __getallfieldNames__():
		return ["Nro_Cuenta","Nro_Tarjeta","Tipo","Nombre_Banco","Postiza MedioPago"]
	def __gettablename__():
		return "Debito"

class Credito(models.Model):
	Nro_Tarjeta = models.IntegerField(primary_key=True,validators=[MaxValueValidator(999999999999999999)])
	Fecha_Vence = models.DateField() 
	Nombre_Banco = models.CharField(max_length=30)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Nro_Tarjeta,self.Fecha_Vence,self.Nombre_Banco,self.Postiza]
	def __getallfieldNames__():
		return ["Nro_Tarjeta","Fecha_Vence","Nombre_Banco","Postiza MedioPago"]
	def __gettablename__():
		return "Credito"

class Transferencia(models.Model):
	Nro_Referencia = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999999999999999999)])
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Nro_Referencia,self.Postiza]
	def __getallfieldNames__():
		return ["Nro_Referencia","Postiza MedioPago"]
	def __gettablename__():
		return "Transferencia"

class Deposito(models.Model):
	Referencia = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999999999999999999)])
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Referencia,self.Postiza]
	def __getallfieldNames__():
		return ["Referencia","Postiza MedioPago"]
	def __gettablename__():
		return "Deposito"
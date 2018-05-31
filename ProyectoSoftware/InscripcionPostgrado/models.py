import datetime
from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Decanato(models.Model):
	Nombre_decanato = models.CharField(primary_key=True, max_length=30,
						validators=[RegexValidator(regex='[a-zA-Z]', message='Nombre incorrecto')])
	def getallfields(self):
		return [self.Nombre_decanato]
	def __getallfieldNames__():
		return ["Nombre_decanato"]
	def __gettablename__():
		return "Decanato"
	def __createElement__(parameters):
		return Decanato(
				Nombre_decanato = parameters["Nombre_decanato"]
			)

class Coordinacion(models.Model):
	Cod_coordinacion = models.CharField(primary_key=True, max_length=2,
										validators=[RegexValidator(regex='[A-Z]{2}', message='Codigo incorrecto')])
	Nombre_coordinacion = models.CharField(max_length=30, validators=[RegexValidator(regex='^([a-zA-Z ])+$', message='Nombre incorrecto')])
	def getallfields(self):
		return [self.Cod_coordinacion,self.Nombre_coordinacion]
	def __str__(self):
		return "%s" % (self.Nombre_coordinacion)
	def __getallfieldNames__():
		return ["Cod_coordinacion","Nombre_coordinacion"]
	def __gettablename__():
		return "Coordinacion"
	def __createElement__(parameters):
		return Coordinacion(
				Cod_coordinacion = parameters["Cod_coordinacion"],
				Nombre_coordinacion = parameters["Nombre_coordinacion"]
			)

class Pertenece(models.Model):
	class Meta:
		unique_together=(('Nombre_decanato', 'Cod_coordinacion'))
	Nombre_decanato = models.ForeignKey(Decanato, on_delete=models.CASCADE)
	Cod_coordinacion = models.ForeignKey(Coordinacion, max_length=2, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Nombre_decanato,self.Cod_coordinacion]
	def __getallfieldNames__():
		return ["Nombre_decanato","Cod_coordinacion"]
	def __gettablename__():
		return "Pertenece"
	def __createElement__(parameters):
		return Decanato(
				Nombre_decanato = parameters["Nombre_decanato"],
				Cod_coordinacion = parameters["Cod_coordinacion"]
			)

class Asignatura(models.Model):
	Cod_asignatura = models.CharField(primary_key=True, max_length=6,
					validators=[RegexValidator(regex='[A-Z]{2}[0-9]{4}', message="Código inválido")])
	Nombre_asig = models.CharField(max_length=30, validators=[RegexValidator(regex='^([a-zA-Z ])+$', message="Nombre inválido")])
	Cod_coordinacion = models.ForeignKey(Coordinacion, max_length=2, on_delete=models.CASCADE)
	Creditos = models.IntegerField(validators=[MaxValueValidator(30, message="Número de creditos inválidos.")])
	Fecha = models.DateField(auto_now_add=True) 
	Visto = models.BooleanField(default=False)
	def getallfields(self):
		return [self.Cod_asignatura,self.Nombre_asig, self.Cod_coordinacion,self.Creditos,self.Visto]
	def __getallfieldNames__():
		return ["Cod_asignatura","Nombre_asig", "Cod_coordinacion", "Creditos", "Fecha", "Visto"]
	def __gettablename__():
		return "Asignatura"
	def __createElement__(parameters):
		return Asignatura(
				Cod_asignatura = parameters["Cod_asignatura"],
				Nombre_asig = parameters["Nombre_asig"],
				Cod_coordinacion = parameters["Cod_coordinacion"],
				Creditos = parameters["Creditos"],
				Fecha = parameters["Fecha"],
				Visto = parameters["Visto"]
			)

class Estudiante(models.Model):
	Carnet = models.CharField(primary_key=True, max_length=8, 
			validators=[RegexValidator(regex='[0-9]{2}\-[0-9]{5}', message='Carnet incorrecto')])
	Apellidos = models.CharField(max_length=30, validators=[RegexValidator(regex='[a-zA-Z]', message='Apellido incorrecto')])
	Nombres = models.CharField(max_length=30, validators=[RegexValidator(regex='[a-zA-Z]', message='Nombre incorrecto')])
	def getallfields(self):
		return [self.Carnet,self.Apellidos,self.Nombres]
	def __getallfieldNames__():
		return ["Carnet","Apellidos","Nombres"]
	def __gettablename__():
		return "Estudiante"
	def __createElement__(parameters):
		return Estudiante(
				Carnet = parameters["Carnet"],
				Apellidos = parameters["Apellidos"],
				Nombres = parameters["Nombres"]
			)

class Profesor(models.Model):
	Id_prof = models.CharField(primary_key=True, max_length=8, validators=[RegexValidator(regex='[0-9]', message='Id incorrecto')])
	Apellidos = models.CharField(max_length=30, validators=[RegexValidator(regex='[a-zA-Z]', message='Apellido incorrecto')])
	Nombres = models.CharField(max_length=30, validators=[RegexValidator(regex='[a-zA-Z]', message='Nombre incorrecto')])
	Cod_coordinacion = models.ForeignKey(Coordinacion, max_length=2, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Id_prof,self.Apellidos,self.Nombres,self.Cod_coordinacion]
	def __getallfieldNames__():
		return ["Id_prof","Apellidos","Nombres","Cod_coordinacion"]
	def __gettablename__():
		return "Profesor"
	def __createElement__(parameters):
		return Profesor(
				Id_prof = parameters["Id_prof"],
				Apellidos = parameters["Apellidos"],
				Nombres = parameters["Nombres"],
				Cod_coordinacion = parameters["Cod_coordinacion"]
			)

def periodo_trimestre_restr(periode):
	if not (periode.lower()=='ene-mar' or periode.lower()=='abr-jul' or periode.lower()=='sep-dic'):
		raise ValidationError(_('Trimestre invalido'))
	return periode

def anio_trimestre_restr(year):
	if not (1970 <= year <= (datetime.date.today().year)+1):
		raise ValidationError(_('Trimestre invalido'))
	return year

class Trimestre(models.Model):
	class Meta:
		unique_together = (('Periodo', 'Anio'))
	Periodo = models.CharField(max_length=20, validators=[periodo_trimestre_restr])
	Anio = models.IntegerField(validators=[anio_trimestre_restr])
	def getallfields(self):
		return [self.Periodo,self.Anio]
	def __getallfieldNames__():
		return ["Periodo","Anio"]
	def __gettablename__():
		return "Trimestre"
	def __createElement__(parameters):
		return Trimestre(
				Periodo = parameters["Periodo"],
				Anio = parameters["Anio"]
			)

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
	def __createElement__(parameters):
		return Cursa(
				Carnet = parameters["Carnet"],
				Cod_asignatura = parameters["Cod_asignatura"],
				Periodo = parameters["Periodo"],
				Anio = parameters["Anio"]
			)

def hora_se_ofrece_restr(hora):
	if not (len(hora)>2):
		raise ValidationError(_('Horario invalido'))
	else:
		horas = hora.split('-')
		if not (0 < int(hora[0]) < int(hora[1]) <14):
			raise ValidationError(_('Horario invalido'))
	return hora

class Se_Ofrece(models.Model):
	class Meta:
		unique_together = (('Id_prof', 'Cod_asignatura','Horario', 'Periodo', 'Anio','Cod_coordinacion'))
	Id_prof = models.ForeignKey(Profesor, primary_key=True, on_delete=models.CASCADE)
	Cod_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
	Horario = models.CharField(max_length=5, validators=[hora_se_ofrece_restr])
	Periodo = models.ForeignKey(Trimestre, related_name='Trimestre_ofrece_periodo', on_delete=models.CASCADE)
	Anio = models.ForeignKey(Trimestre, related_name='Trimestre_ofrece_anio', on_delete=models.CASCADE)
	Cod_coordinacion = models.ForeignKey(Coordinacion, max_length=2, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Id_prof,self.Cod_asignatura,self.Horario,self.Periodo,self.Anio, self.Cod_coordinacion]
	def __getallfieldNames__():
		return ["Id_prof","Cod_asignatura","Horario","Periodo","Anio", "Cod_coordinacion"]
	def __gettablename__():
		return "Se_Ofrece"
	def __createElement__(parameters):
		return Se_Ofrece(
				Id_prof = parameters["Id_prof"],
				Cod_asignatura = parameters["Cod_asignatura"],
				Horario = parameters["Horario"],
				Periodo = parameters["Periodo"],
				Anio = parameters["Anio"],
				Cod_coordinacion = parameters["Cod_coordinacion"]
			)


class MedioPago(models.Model):
	Postiza = models.AutoField(primary_key=True)
	def getallfields(self):
		return [self.Postiza]
	def __getallfieldNames__():
		return ["Postiza"]
	def __gettablename__():
		return "MedioPago"
	def __createElement__(parameters):
		return MedioPago(
				Postiza=parameters["Postiza"]
			)

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
		return ["Precio","Carnet","Postiza","Periodo","Anio"]
	def __gettablename__():
		return "Paga_Con"
	def __createElement__(parameters):
		return Paga_Con(
				Precio = parameters["Precio"],
				Carnet = parameters["Carnet"],
				Postiza = parameters["Postiza"],
				Periodo = parameters["Periodo"],
				Anio = parameters["Anio"]
			)

def tipo_debito_restr(type):
	if not (type.lower()=="ahorro" or type.lower()=="corriente"):
		raise ValidationError(_('Tipo de cuenta invalido'))
	return type

class Debito(models.Model):
	Nro_Cuenta = models.CharField(primary_key=True, max_length = 20,validators = [RegexValidator(regex='[0-9]{20}', message='Nro cuenta incorrecto')])
	Nro_Tarjeta = models.CharField(max_length = 18,validators=[RegexValidator(regex='[0-9]{18}', message='Nro tarjeta incorrecto')])
	Tipo = models.CharField(max_length=9, validators=[tipo_debito_restr])
	Nombre_Banco = models.CharField(max_length=30)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Nro_Cuenta,self.Nro_Tarjeta,self.Tipo,self.Nombre_Banco,self.Postiza]
	def __getallfieldNames__():
		return ["Nro_Cuenta","Nro_Tarjeta","Tipo","Nombre_Banco","Postiza"]
	def __gettablename__():
		return "Debito"
	def __createElement__(parameters):
		return Debito(
				Nro_Cuenta = parameters["Nro_Cuenta"],
				Nro_Tarjeta = parameters["Nro_Tarjeta"],
				Tipo = parameters["Tipo"],
				Nombre_Banco = parameters["Nombre_Banco"],
				Postiza = parameters["Postiza"]
			)

class Credito(models.Model):
	Nro_Tarjeta = models.CharField(primary_key=True,max_length = 18,validators=[RegexValidator(regex='[0-9]{18}', message='Nro tarjeta incorrecto')])
	Fecha_Vence = models.DateField() 
	Nombre_Banco = models.CharField(max_length=30)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Nro_Tarjeta,self.Fecha_Vence,self.Nombre_Banco,self.Postiza]
	def __getallfieldNames__():
		return ["Nro_Tarjeta","Fecha_Vence","Nombre_Banco","Postiza"]
	def __gettablename__():
		return "Credito"
	def __createElement__(parameters):
		return Credito(
				Nro_Tarjeta = parameters["Nro_Tarjeta"],
				Fecha_Vence = parameters["Fecha_Vence"],
				Nombre_Banco = parameters["Nombre_Banco"],
				Postiza = parameters["Postiza"]
			)

class Transferencia(models.Model):
	Nro_Referencia = models.CharField(primary_key=True,max_length = 20, validators=[RegexValidator(regex='[0-9]{20}', message='Nro Referencia incorrecto')])
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Nro_Referencia,self.Postiza]
	def __getallfieldNames__():
		return ["Nro_Referencia","Postiza"]
	def __gettablename__():
		return "Transferencia"
	def __createElement__(parameters):
		return Debito(
				Nro_Referencia = parameters["Nro_Referencia"],
				Postiza = parameters["Postiza"]
			)

class Deposito(models.Model):
	Referencia = models.CharField(primary_key=True, max_length = 20, validators=[RegexValidator(regex='[0-9]{20}', message='Nro Referencia incorrecto')])
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Referencia,self.Postiza]
	def __getallfieldNames__():
		return ["Referencia","Postiza"]
	def __gettablename__():
		return "Deposito"
	def __createElement__(parameters):
		return Debito(
				Referencia = parameters["Referencia"],
				Postiza = parameters["Postiza"]
			)
import datetime
import re
from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Tabla de los decanatos.
class Decanato(models.Model):
	Nombre_decanato = models.CharField(primary_key=True, max_length=30,
						validators=[RegexValidator(regex='[a-zA-Z]', message='Nombre incorrecto')])
	def getallfields(self):
		return [self.Nombre_decanato]
	def __getallfieldNames__(self):
		return ["Nombre_decanato"]
	def __gettablename__(self):
		return "Decanato"
	def __createElement__(self,parameters):
		return Decanato(
				Nombre_decanato = parameters["Nombre_decanato"]
			)

# Tabla de las coordinaciones, tiene el codigo y el nombre.
class Coordinacion(models.Model):
	Cod_coordinacion = models.CharField(primary_key=True, max_length=2,
										validators=[RegexValidator(regex='[A-Z]{2}', message='Codigo incorrecto')])
	Nombre_coordinacion = models.CharField(max_length=30, validators=[RegexValidator(re.compile('^[\w+\s]+$'), _('Nombre incorrecto'), 'invalid')])
	def getallfields(self):
		return [self.Cod_coordinacion,self.Nombre_coordinacion]
	def __str__(self):
		return "%s" % (self.Nombre_coordinacion)
	def __getallfieldNames__(self):
		return ["Cod_coordinacion","Nombre_coordinacion"]
	def __gettablename__(self):
		return "Coordinacion"
	def __createElement__(self,parameters):
		return Coordinacion(
				Cod_coordinacion = parameters["Cod_coordinacion"],
				Nombre_coordinacion = parameters["Nombre_coordinacion"]
			)

# Tabla de relacion de Coordinacion pertenece a Decanato.
class Pertenece(models.Model):
	class Meta:
		unique_together=(('Nombre_decanato', 'Cod_coordinacion'))
	Nombre_decanato = models.ForeignKey(Decanato, on_delete=models.CASCADE)
	Cod_coordinacion = models.ForeignKey(Coordinacion, max_length=2, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Nombre_decanato,self.Cod_coordinacion]
	def __getallfieldNames__(self):
		return ["Nombre_decanato","Cod_coordinacion"]
	def __gettablename__(self):
		return "Pertenece"
	def __createElement__(self,parameters):
		return Decanato(
				Nombre_decanato = parameters["Nombre_decanato"],
				Cod_coordinacion = parameters["Cod_coordinacion"]
			)

# Tabla de Asignaturas que contiene el codigo, nombre, creditos, fecha de creacion, visto y el link del programa.
class Asignatura(models.Model):
	Cod_asignatura = models.CharField(primary_key=True, max_length=7,
					validators=[RegexValidator(regex='[A-Z]{2}-[0-9]{4}', message="Código inválido")])
	Nombre_asig = models.CharField(max_length=250, validators=[RegexValidator(re.compile('^[\w+\s]+$'), _('Nombre inválido'), 'invalid')])
		#validators=[RegexValidator(regex='^\w+$', message="Nombre inválido")])
	Cod_coordinacion = models.ForeignKey(Coordinacion, max_length=2, on_delete=models.CASCADE)
	Creditos = models.IntegerField(validators=[MaxValueValidator(30, message="Número de creditos inválidos."),MinValueValidator(1,message="Número de creditos inválidos.")])
	Fecha = models.DateField(auto_now_add=True) 
	Visto = models.BooleanField(default=False)
	Programa = models.URLField()
	def getallfields(self):
		return [self.Cod_asignatura,self.Nombre_asig, self.Cod_coordinacion,self.Creditos,self.Fecha,self.Visto,self.Programa]
	def __getallfieldNames__(self):
		return ["Cod_asignatura","Nombre_asig", "Cod_coordinacion", "Creditos", "Fecha", "Visto", "Programa"]
	def __gettablename__(self):
		return "Asignatura"
	def __createElement__(self,parameters):
		return Asignatura(
				Cod_asignatura = parameters["Cod_asignatura"],
				Nombre_asig = parameters["Nombre_asig"],
				Cod_coordinacion = parameters["Cod_coordinacion"],
				Creditos = parameters["Creditos"],
				Fecha = parameters["Fecha"],
				Visto = parameters["Visto"],
				Programa = parameters["Programa"]
			)
	def __str__(self):
		return str(self.Cod_asignatura) + " "  +  str(self.Nombre_asig) + " " + str(self.Cod_coordinacion) + " " + str(self.Creditos)

# Tabla de estudiantes, tiene carnet, apellidos y nombres.
class Estudiante(models.Model):
	Carnet = models.CharField(primary_key=True, max_length=8, 
			validators=[RegexValidator(regex='[0-9]{2}\-[0-9]{5}', message='Carnet incorrecto')])
	Apellidos = models.CharField(max_length=30, validators=[RegexValidator(re.compile('^[\w+\s]+$'), _('Apellido incorrecto'), 'invalid')])
	Nombres = models.CharField(max_length=30, validators=[RegexValidator(re.compile('^[\w+\s]+$'), _('Nombre incorrecto'), 'invalid')])
	def getallfields(self):
		return [self.Carnet,self.Apellidos,self.Nombres]
	def __getallfieldNames__(self):
		return ["Carnet","Apellidos","Nombres"]
	def __gettablename__(self):
		return "Estudiante"
	def __createElement__(self,parameters):
		return Estudiante(
				Carnet = parameters["Carnet"],
				Apellidos = parameters["Apellidos"],
				Nombres = parameters["Nombres"]
			)

# Tabla de profesores, tiene todos los datos de los profesores.
class Profesor(models.Model):
	Id_prof = models.CharField(primary_key=True, max_length=8, validators=[RegexValidator(regex='[0-9]', message='Id incorrecto')])
	Apellidos = models.CharField(max_length=30, validators=[RegexValidator(re.compile('^[^\W\d_]+\s$'), _('Apellido incorrecto'), 'invalid')])
	Nombres = models.CharField(max_length=30, validators=[RegexValidator(re.compile('^[^\W\d_]+\s$'), _('Nombre incorrecto'), 'invalid')])
	Cod_coordinacion = models.ForeignKey(Coordinacion, max_length=2, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Id_prof,self.Apellidos,self.Nombres,self.Cod_coordinacion]
	def __getallfieldNames__(self):
		return ["Id_prof","Apellidos","Nombres","Cod_coordinacion"]
	def __gettablename__(self):
		return "Profesor"
	def __createElement__(self,parameters):
		return Profesor(
				Id_prof = parameters["Id_prof"],
				Apellidos = parameters["Apellidos"],
				Nombres = parameters["Nombres"],
				Cod_coordinacion = parameters["Cod_coordinacion"]
			)

# Funcion que indica los campos permitidos en el nombre del periodo.
def periodo_trimestre_restr(periode):
	if not (periode.lower()=='ene-mar' or periode.lower()=='abr-jul' or periode.lower()=='sep-dic'):
		raise ValidationError(_('Trimestre invalido'))
	return periode

# Funcion que indica los campos permitidos en el año del periodo.
def anio_trimestre_restr(year):
	if not (1970 <= year <= (datetime.date.today().year)+1):
		raise ValidationError(_('Trimestre invalido'))
	return year

# Tabla de los trimestre, cuya clave es (periodo, anio)
class Trimestre(models.Model):
	class Meta:
		unique_together = (('Periodo', 'Anio'))
	Periodo = models.CharField(max_length=20, validators=[periodo_trimestre_restr])
	Anio = models.IntegerField(validators=[anio_trimestre_restr])
	def getallfields(self):
		return [self.Periodo,self.Anio]
	def __getallfieldNames__(self):
		return ["Periodo","Anio"]
	def __gettablename__(self):
		return "Trimestre"
	def __createElement__(self,parameters):
		return Trimestre(
				Periodo = parameters["Periodo"],
				Anio = parameters["Anio"]
			)

# Tabla de relacion de cursa, Estudiante cursa asignatura en trimestre.
class Cursa(models.Model):
	class Meta:
		unique_together=(('Carnet', 'Cod_asignatura', 'Periodo', 'Anio'))
	Carnet = models.ForeignKey(Estudiante, primary_key=True, on_delete=models.CASCADE)
	Cod_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
	Periodo = models.ForeignKey(Trimestre, related_name='Trimestre_cursa_periodo', on_delete=models.CASCADE)
	Anio = models.ForeignKey(Trimestre, related_name='Trimestre_cursa_anio', on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Carnet,self.Cod_asignatura,self.Periodo,self.Anio]
	def __getallfieldNames__(self):
		return ["Carnet","Cod_asignatura","Periodo","Anio"]
	def __gettablename__(self):
		return "Cursa"
	def __createElement__(self,parameters):
		return Cursa(
				Carnet = parameters["Carnet"],
				Cod_asignatura = parameters["Cod_asignatura"],
				Periodo = parameters["Periodo"],
				Anio = parameters["Anio"]
			)

# Funcion que verifica si el formato de la hora es valido.
def hora_se_ofrece_restr(hora):
	# if not (len(hora)>3):
	# 	raise ValidationError(_('Horario invalido'))
	# else:
	hora = hora.split('-')
	if not (0 < int(hora[0]) < int(hora[1]) <14):
		raise ValidationError(_('Horario invalido'))
	return hora

# Tabla de relacion se_ofrece, Coordinacion ofrece asignatura en trimestre con profesor.  
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
	def __getallfieldNames__(self):
		return ["Id_prof","Cod_asignatura","Horario","Periodo","Anio", "Cod_coordinacion"]
	def __gettablename__(self):
		return "Se_Ofrece"
	def __createElement__(self,parameters):
		return Se_Ofrece(
				Id_prof = parameters["Id_prof"],
				Cod_asignatura = parameters["Cod_asignatura"],
				Horario = parameters["Horario"],
				Periodo = parameters["Periodo"],
				Anio = parameters["Anio"],
				Cod_coordinacion = parameters["Cod_coordinacion"]
			)

# Tabla de Medio Pago
class MedioPago(models.Model):
	Postiza = models.AutoField(primary_key=True)
	def getallfields(self):
		return [self.Postiza]
	def __getallfieldNames__(self):
		return ["Postiza"]
	def __gettablename__(self):
		return "MedioPago"
	def __createElement__(self,parameters):
		return MedioPago(
				Postiza=parameters["Postiza"]
			)

# Tabla relacion de Paga_con, Estudiante paga con medio de pago la inscripcion del trimestre
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
	def __getallfieldNames__(self):
		return ["Precio","Carnet","Postiza","Periodo","Anio"]
	def __gettablename__(self):
		return "Paga_Con"
	def __createElement__(self,parameters):
		return Paga_Con(
				Precio = parameters["Precio"],
				Carnet = parameters["Carnet"],
				Postiza = parameters["Postiza"],
				Periodo = parameters["Periodo"],
				Anio = parameters["Anio"]
			)

# Funcion que indica los campos permitidos en el tipo de tarjeta de debito.
def tipo_debito_restr(tipo):
	if not (tipo.lower()=="ahorro" or tipo.lower()=="corriente"):
		raise ValidationError(_('Tipo de cuenta invalido'))
	return tipo

# Tabla de Tarjeta de debito
class Debito(models.Model):
	Nro_Cuenta = models.CharField(primary_key=True, max_length = 20,validators = [RegexValidator(regex='[0-9]{20}', message='Nro cuenta incorrecto')])
	Nro_Tarjeta = models.CharField(max_length = 18,validators=[RegexValidator(regex='[0-9]{18}', message='Nro tarjeta incorrecto')])
	Tipo = models.CharField(max_length=9, validators=[tipo_debito_restr])
	Nombre_Banco = models.CharField(max_length=30)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Nro_Cuenta,self.Nro_Tarjeta,self.Tipo,self.Nombre_Banco,self.Postiza]
	def __getallfieldNames__(self):
		return ["Nro_Cuenta","Nro_Tarjeta","Tipo","Nombre_Banco","Postiza"]
	def __gettablename__(self):
		return "Debito"
	def __createElement__(self,parameters):
		return Debito(
				Nro_Cuenta = parameters["Nro_Cuenta"],
				Nro_Tarjeta = parameters["Nro_Tarjeta"],
				Tipo = parameters["Tipo"],
				Nombre_Banco = parameters["Nombre_Banco"],
				Postiza = parameters["Postiza"]
			)

# Tabla de tarjeta de credito.
class Credito(models.Model):
	Nro_Tarjeta = models.CharField(primary_key=True,max_length = 18,validators=[RegexValidator(regex='[0-9]{18}', message='Nro tarjeta incorrecto')])
	Fecha_Vence = models.DateField() 
	Nombre_Banco = models.CharField(max_length=30)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Nro_Tarjeta,self.Fecha_Vence,self.Nombre_Banco,self.Postiza]
	def __getallfieldNames__(self):
		return ["Nro_Tarjeta","Fecha_Vence","Nombre_Banco","Postiza"]
	def __gettablename__(self):
		return "Credito"
	def __createElement__(self,parameters):
		return Credito(
				Nro_Tarjeta = parameters["Nro_Tarjeta"],
				Fecha_Vence = parameters["Fecha_Vence"],
				Nombre_Banco = parameters["Nombre_Banco"],
				Postiza = parameters["Postiza"]
			)

# Tabla de las tranferencias.
class Transferencia(models.Model):
	Nro_Referencia = models.CharField(primary_key=True,max_length = 20, validators=[RegexValidator(regex='[0-9]{20}', message='Nro Referencia incorrecto')])
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Nro_Referencia,self.Postiza]
	def __getallfieldNames__(self):
		return ["Nro_Referencia","Postiza"]
	def __gettablename__(self):
		return "Transferencia"
	def __createElement__(self,parameters):
		return Debito(
				Nro_Referencia = parameters["Nro_Referencia"],
				Postiza = parameters["Postiza"]
			)

#Tabla de los depositos.
class Deposito(models.Model):
	Referencia = models.CharField(primary_key=True, max_length = 20, validators=[RegexValidator(regex='[0-9]{20}', message='Nro Referencia incorrecto')])
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Referencia,self.Postiza]
	def __getallfieldNames__(self):
		return ["Referencia","Postiza"]
	def __gettablename__(self):
		return "Deposito"
	def __createElement__(self,parameters):
		return Debito(
				Referencia = parameters["Referencia"],
				Postiza = parameters["Postiza"]
			)
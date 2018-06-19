import datetime
import re
from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class Decanato(models.Model):
	""" Consiste en la tabla de los decanatos.
	Parametros:
		models.Model (Decanato): es la instancia sobre la que se crea la tabla.

	Atributos de la clase: 
		Nombre_decanato : nombre del decanato.
	"""
	Nombre_decanato = models.CharField(primary_key=True, max_length=30,
						validators=[RegexValidator(regex='[a-zA-Z]', message='Nombre incorrecto')])
	def getallfields(self):
		""" Devuelve los atributos de la clase """
		return [self.Nombre_decanato]
	def __getallfieldNames__(self):
		""" Obtiene los nombres de los atributos de la clase"""
		return ["Nombre_decanato"]
	def __gettablename__(self):
		""" Obtiene el nombre de la clase"""
		return "Decanato"
	def __createElement__(self,parameters):
		""" Crea y retorna un nuevo nodo o elemento de la tabla"""
		return Decanato(
				Nombre_decanato = parameters["Nombre_decanato"]
			)

class Coordinacion(models.Model):
	""" Consiste en la tabla de las coordinaciones.
	Parametros:
		models.Model (Coordinacion): es la instancia sobre la que se crea la tabla.

	Atributos de la clase: 
		Cod_coordinacion : Codigo de la coordinacion.
		Nombre_coordinacion : Nombre de la coordinacion.
	"""
	Cod_coordinacion = models.CharField(primary_key=True, max_length=2,
										validators=[RegexValidator(regex='[A-Z]{2}', message='Codigo incorrecto')])
	Nombre_coordinacion = models.CharField(max_length=30, validators=[RegexValidator(re.compile('^[\w+\s]+$'), _('Nombre incorrecto'), 'invalid')])
	def getallfields(self):
		""" Devuelve los atributos de la clase """
		return [self.Cod_coordinacion,self.Nombre_coordinacion]
	def __str__(self):
		return "%s" % (self.Nombre_coordinacion)
	def __getallfieldNames__(self):
		""" Obtiene los nombres de los atributos de la clase"""
		return ["Cod_coordinacion","Nombre_coordinacion"]
	def __gettablename__(self):
		""" Obtiene el nombre de la clase"""
		return "Coordinacion"
	def __createElement__(self,parameters):
		""" Crea y retorna un nuevo nodo o elemento de la tabla"""
		return Coordinacion(
				Cod_coordinacion = parameters["Cod_coordinacion"],
				Nombre_coordinacion = parameters["Nombre_coordinacion"]
			)

class Pertenece(models.Model):
	""" Consiste en la tabla de la relacion Pertenece.
	Parametros:
		models.Model (Pertenece): es la instancia sobre la que se crea la tabla.

	Atributos de la clase: 
		Cod_coordinacion : Codigo de la coordinacion.
		Nombre_decanato : Nombre del decanato.
	"""
	class Meta:
		unique_together=(('Nombre_decanato', 'Cod_coordinacion'))
	Nombre_decanato = models.ForeignKey(Decanato, on_delete=models.CASCADE)
	Cod_coordinacion = models.ForeignKey(Coordinacion, max_length=2, on_delete=models.CASCADE)
	def getallfields(self):
		""" Devuelve los atributos de la clase """
		return [self.Nombre_decanato,self.Cod_coordinacion]
	def __getallfieldNames__(self):
		""" Obtiene los nombres de los atributos de la clase"""
		return ["Nombre_decanato","Cod_coordinacion"]
	def __gettablename__(self):
		""" Obtiene el nombre de la clase"""
		return "Pertenece"
	def __createElement__(self,parameters):
		""" Crea y retorna un nuevo nodo o elemento de la tabla"""
		return Decanato(
				Nombre_decanato = parameters["Nombre_decanato"],
				Cod_coordinacion = parameters["Cod_coordinacion"]
			)

class Asignatura(models.Model):
	""" Consiste en la tabla de las asignaturas.
	Parametros:
		models.Model (Asignatura): es la instancia sobre la que se crea la tabla.

	Atributos de la clase: 
		Cod_asignatura :  Codigo de la asignatura.
		Nombre_asig : Nombre de la asignatura.
		Cod_coordinacion : Codigo de la coordinacion.
		Creditos : Cantidad de creditos de la asignatura.
		Fecha : Fecha en que se creo o modifico la asignatura.
		Visto : Valor booleano que indica si fue vista o no.
		Programa : Link del programa de la asignatura.
	"""
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
		""" Devuelve los atributos de la clase """
		return [self.Cod_asignatura,self.Nombre_asig, self.Cod_coordinacion,self.Creditos,self.Fecha,self.Visto,self.Programa]
	def __getallfieldNames__(self):
		""" Obtiene los nombres de los atributos de la clase"""
		return ["Cod_asignatura","Nombre_asig", "Cod_coordinacion", "Creditos", "Fecha", "Visto", "Programa"]
	def __gettablename__(self):
		""" Obtiene el nombre de la clase"""
		return "Asignatura"
	def __createElement__(self,parameters):
		""" Crea y retorna un nuevo nodo o elemento de la tabla"""
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
		return str(self.Cod_asignatura) + " "  +  str(self.Nombre_asig)[0:35] + "..."

class Estudiante(models.Model):
	""" Consiste en la tabla de los estudiantes.
	Parametros:
		models.Model (Estudiante): es la instancia sobre la que se crea la tabla.

	Atributos de la clase: 
		Carnet : carnet del estudiante.
		Apellidos : Apellidos del estudiante.
		Nombres : Nombres del estudiante.
	"""
	Carnet = models.CharField(primary_key=True, max_length=8, 
			validators=[RegexValidator(regex='[0-9]{2}\-[0-9]{5}', message='Carnet incorrecto')])
	Apellidos = models.CharField(max_length=30, validators=[RegexValidator(re.compile('^[\w+\s]+$'), _('Apellido incorrecto'), 'invalid')])
	Nombres = models.CharField(max_length=30, validators=[RegexValidator(re.compile('^[\w+\s]+$'), _('Nombre incorrecto'), 'invalid')])
	def getallfields(self):
		""" Devuelve los atributos de la clase """
		return [self.Carnet,self.Apellidos,self.Nombres]
	def __getallfieldNames__(self):
		""" Obtiene los nombres de los atributos de la clase"""
		return ["Carnet","Apellidos","Nombres"]
	def __gettablename__(self):
		""" Obtiene el nombre de la clase"""
		return "Estudiante"
	def __createElement__(self,parameters):
		""" Crea y retorna un nuevo nodo o elemento de la tabla"""
		return Estudiante(
				Carnet = parameters["Carnet"],
				Apellidos = parameters["Apellidos"],
				Nombres = parameters["Nombres"]
			)

def nombre_profesor_restr(nombres):
	""" Verifica si el largo del nombre de los profesores son mayor a 0. 
    Devuelve los nombres correspondiente.

    Parámetros:
    nombres -- Nombres de los profesores.

    Excepciones:
    ValidationError -- Si no cumple condicion antes mencionada.
    """
	if (len(nombres)<1):
		raise ValidationError(_('Nombre invalido'))
	return nombres

def apellido_profesor_restr(apellidos):
	""" Verifica si el largo de los apellidos de los profesores son mayor a 0. 
    Devuelve los nombres correspondiente.

    Parámetros:
    apellidos -- Apellidos de los profesores.

    Excepciones:
    ValidationError -- Si no cumple condicion antes mencionada.
    """
	if (len(apellidos)<1):
		raise ValidationError(_('Apellido invalido'))
	return apellidos

class Profesor(models.Model):
	""" Consiste en la tabla de los profesores.
	Parametros:
		models.Model (Profesor): es la instancia sobre la que se crea la tabla.

	Atributos de la clase: 
		Id_prof : carnet del profesor.
		Apellidos : Apellidos del profesor.
		Nombres : Nombres del profesor.
		Cod_coordinacion : Codigo de la coordinacion en que trabaja.
	"""
	min_length=1
	Id_prof = models.CharField(primary_key=True, max_length=8, validators=[RegexValidator(regex='^[0-9]+$', message='Id incorrecto')])
	Apellidos = models.CharField(max_length=30,  validators=[RegexValidator(re.compile('^[\w+\s]+[^\W\d_]+$'), _('Apellido incorrecto'), 'invalid')])
	Nombres = models.CharField(max_length=30, validators=[nombre_profesor_restr,RegexValidator(re.compile('^[\w+\s]+[^\W\d_]+$'), _('Nombre incorrecto'), 'invalid')])
	Cod_coordinacion = models.ForeignKey(Coordinacion, max_length=2, on_delete=models.CASCADE)
	def getallfields(self):
		""" Devuelve los atributos de la clase """
		return [self.Id_prof,self.Apellidos,self.Nombres,self.Cod_coordinacion]
	def __getallfieldNames__(self):
		""" Obtiene los nombres de los atributos de la clase"""
		return ["Id_prof","Apellidos","Nombres","Cod_coordinacion"]
	def __gettablename__(self):
		""" Obtiene el nombre de la clase"""
		return "Profesor"
	def __createElement__(self,parameters):
		""" Crea y retorna un nuevo nodo o elemento de la tabla"""
		return Profesor(
				Id_prof = parameters["Id_prof"],
				Apellidos = parameters["Apellidos"],
				Nombres = parameters["Nombres"],
				Cod_coordinacion = parameters["Cod_coordinacion"]
			)
	def __str__(self):
		return "Prof. "  +  str(self.Nombres) + " " + str(self.Apellidos) + " C.I." + str(self.Id_prof)

def horario_formato(hora):
	""" Transforma el formato de la hora, en el deseado.

    Devuelve en un string del horario con el siguiente formato:
        hora1 (am/pm) - hora2 (am/pm).

    Parámetros:
    hora -- string de hora correspondiente a la oferta de materias.
    """
	hora = hora.split('-')
	formato1 = (int(hora[0])+6)%12 
	formato2 = (int(hora[1])+6)%12
	
	if int(hora[0])<6:
		str1 = str(formato1)+':30 am'
	else:
		str1 = str(formato1)+':30 pm'
	if int(hora[1])<6:
		str2 = str(formato2)+':30 am'
	else:
		str2 = str(formato2)+':30 pm'

	return str1+'-'+str2

def anio_trimestre_restr(year):
	""" Verifica si anio ingresado es valido. 
	Comprueba si el valor esta entre: 1970 y el anio proximo al actual.
    Devuelve el anio correspondiente.

    Parámetros:
    year -- Anio en del trimestre a registrar.

    Excepciones:
    ValidationError -- Si no cumple condicion antes mencionada.
    """
	if not (1970 <= year <= (datetime.date.today().year)+1):
		raise ValidationError(_('Trimestre invalido'))
	return year

# Tabla de los trimestre, cuya clave es (periodo, anio)
class Trimestre(models.Model):
	TRIMESTRE_CHOICES = (
        ('EM', 'ENE-MAR'),
        ('AJ', 'ABR-JUL'),
        ('V', 'VERANO'),
        ('SD', 'SEP-DIC')
    )
	class Meta:
		unique_together = (('Periodo', 'Anio'))
	Periodo = models.CharField(max_length=7, choices=TRIMESTRE_CHOICES)
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
	def returnTrimestre(self):
		""" Devuelve las opciones de los trimestres para las ofertas"""
		if "EM" in self.Periodo:
			return "ENE-MAR"
		elif "AJ" in self.Periodo:
			return "ABR-JUL"
		elif "V" in self.Periodo:
			return "VERANO"
		else:
			return "SEPT-DIC"
	
class Cursa(models.Model):
	""" Consiste en la tabla de la relacion de cursa.
	Parametros:
		models.Model (Cursa): es la instancia sobre la que se crea la tabla.

	Atributos de la clase: 
		Carnet : carnet del estudiante.
		Cod_asignatura : Codigo de la asignatura a cursar.
		Periodo : periodo del trimestre a cursar.
		Anio : anio del trimestre a cursar.
	"""
	TRIMESTRE_CHOICES = (
        ('EM', 'ENE-MAR'),
        ('AJ', 'ABR-JUL'),
        ('V', 'VERANO'),
        ('SD', 'SEP-DIC')
    )
	class Meta:
		unique_together=(('Carnet', 'Cod_asignatura', 'Periodo', 'Anio'))
	Carnet = models.ForeignKey(Estudiante, primary_key=True, on_delete=models.CASCADE)
	Cod_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
	Periodo = models.CharField(max_length = 7,choices=TRIMESTRE_CHOICES)
	Anio = models.IntegerField(validators=[anio_trimestre_restr])
	def getallfields(self):
		""" Devuelve los atributos de la clase """
		return [self.Carnet,self.Cod_asignatura,self.Periodo,self.Anio]
	def __getallfieldNames__(self):
		""" Obtiene los nombres de los atributos de la clase"""
		return ["Carnet","Cod_asignatura","Periodo","Anio"]
	def __gettablename__(self):
		""" Obtiene el nombre de la clase"""
		return "Cursa"
	def __createElement__(self,parameters):
		""" Crea y retorna un nuevo nodo o elemento de la tabla"""
		return Cursa(
				Carnet = parameters["Carnet"],
				Cod_asignatura = parameters["Cod_asignatura"],
				Periodo = parameters["Periodo"],
				Anio = parameters["Anio"]
			)

def hora_se_ofrece_restr(hora):
	""" Verifica si horario ingresado es valido. 
	Comprueba si el valor esta entre: 1 y el 13.
    Devuelve el horario correspondiente.

    Parámetros:
    hora -- Horario en de la asignatura a registrar.

    Excepciones:
    ValidationError -- Si no cumple condicion antes mencionada.
    """
	hora = hora.split('-')
	if not (0 < int(hora[0]) < int(hora[1]) <14):
		raise ValidationError(_('Horario invalido'))
	return hora

class Se_Ofrece(models.Model):
	""" Consiste en la tabla de la relacion de los ofertas.
	Parametros:
		models.Model (Se_Ofrece): es la instancia sobre la que se crea la tabla.

	Atributos de la clase: 
		Id_prof : carnet del profesor.
		Cod_asignatura : Codigo de la asignatura ofertada.
		Horario : Horario en que se oferta la materia. 
		Dia : dia de la semana.
		Periodo : periodo de la oferta.
		Cod_coordinacion : Codigo de la coordinacion en que oferta.
	"""
	DAY_CHOICES = (
        ('LUNES', 'Lunes'),
        ('MARTES', 'Martes'),
        ('MIERCOLES', 'Miércoles'),
        ('JUEVES', 'Jueves'),
		('VIERNES', 'Viernes'),
		('SABADO', 'Sábado')
    )
	class Meta:
		unique_together = (('Id_prof', 'Cod_asignatura','Horario', 'Periodo', 'Cod_coordinacion'))
	Id_prof = models.ForeignKey(Profesor, on_delete=models.CASCADE)
	Cod_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
	Horario = models.CharField(max_length=5, validators=[hora_se_ofrece_restr])
	Dia = models.CharField(max_length = 9,choices=DAY_CHOICES)
	Periodo = models.ForeignKey(Trimestre, related_name='Trimestre_ofrece_periodo', on_delete=models.CASCADE)
	Cod_coordinacion = models.ForeignKey(Coordinacion, max_length=2, on_delete=models.CASCADE)
	def getallfields(self):
		""" Devuelve los atributos de la clase """
		return [self.Id_prof,self.Cod_asignatura,self.Horario,self.Periodo, self.Cod_coordinacion]
	def __getallfieldNames__(self):
		""" Obtiene los nombres de los atributos de la clase"""
		return ["Id_prof","Cod_asignatura","Horario", "Cod_coordinacion"]
	def __gettablename__(self):
		""" Obtiene el nombre de la clase"""
		return "Se_Ofrece"
	def __createElement__(self,parameters):
		""" Crea y retorna un nuevo nodo o elemento de la tabla"""
		return Se_Ofrece(
				Id_prof = parameters["Id_prof"],
				Cod_asignatura = parameters["Cod_asignatura"],
				Horario = parameters["Horario"],
				Dia = parameters["Dia"],
				Periodo = parameters["Periodo"],
				Anio = parameters["Anio"],
				Cod_coordinacion = parameters["Cod_coordinacion"]
			)
	def returnTime(self):
		"""Retorna el horario """
		return horario_formato(self.Horario)
	def returnDiaMinus(self):
		"""Devuelve el dia de la semana en que se oferta materia"""
		return self.Dia.title()

class MedioPago(models.Model):
	""" Consiste en la tabla del medio de pago.
	Parametros:
		models.Model (MedioPago): es la instancia sobre la que se crea la tabla.

	Atributos de la clase: 
		Postiza : Valor identificador del medio de pago.
	"""
	Postiza = models.AutoField(primary_key=True)
	def getallfields(self):
		""" Devuelve los atributos de la clase """
		return [self.Postiza]
	def __getallfieldNames__(self):
		""" Obtiene los nombres de los atributos de la clase"""
		return ["Postiza"]
	def __gettablename__(self):
		""" Obtiene el nombre de la clase"""
		return "MedioPago"
	def __createElement__(self,parameters):
		""" Crea y retorna un nuevo nodo o elemento de la tabla"""
		return MedioPago(
				Postiza=parameters["Postiza"]
			)

class Paga_Con(models.Model):
	""" Consiste en la tabla de la relacion de Paga_con
		models.Model (Paga_Con): es la instancia sobre la que se crea la tabla.

	Atributos de la clase: 
		Precio : precio de la inscripcion del trimestre.
		Carnet : carnet del estudiante
		Postiza : id del medio de pago
		Periodo : periodo del trimestre.
		Anio : anio del trimestre.
	"""
	TRIMESTRE_CHOICES = (
        ('EM', 'ENE-MAR'),
        ('AJ', 'ABR-JUL'),
        ('V', 'VERANO'),
        ('SD', 'SEP-DIC')
    )
	class Meta:
		unique_together = (('Carnet', 'Postiza', 'Periodo', 'Anio'))
	Precio = models.DecimalField(max_digits=19, decimal_places=4)
	Carnet = models.ForeignKey(Estudiante, primary_key=True, on_delete=models.CASCADE)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	Periodo = models.CharField(max_length=7, choices=TRIMESTRE_CHOICES)
	Anio = models.IntegerField(validators=[anio_trimestre_restr])
	def getallfields(self):
		""" Devuelve los atributos de la clase """
		return [self.Precio,self.Carnet,self.Cod_asignatura,self.Periodo,self.Anio]
	def __getallfieldNames__(self):
		""" Obtiene los nombres de los atributos de la clase"""
		return ["Precio","Carnet","Postiza","Periodo","Anio"]
	def __gettablename__(self):
		""" Obtiene el nombre de la clase"""
		return "Paga_Con"
	def __createElement__(self,parameters):
		""" Crea y retorna un nuevo nodo o elemento de la tabla"""
		return Paga_Con(
				Precio = parameters["Precio"],
				Carnet = parameters["Carnet"],
				Postiza = parameters["Postiza"],
				Periodo = parameters["Periodo"],
				Anio = parameters["Anio"]
			)

def tipo_debito_restr(tipo):
	""" Indica los campos permitidos al ingresar el tipo de tarjeta. 
	Comprueba si el valor esta es: "ahorro" o "corriente".
    Devuelve el tipo correspondiente.

    Parámetros:
    tipo -- Tipo de tarjeta de debito.

    Excepciones:
    ValidationError -- Si no cumple condicion antes mencionada.
    """
	if not (tipo.lower()=="ahorro" or tipo.lower()=="corriente"):
		raise ValidationError(_('Tipo de cuenta invalido'))
	return tipo

class Debito(models.Model):
	""" Consiste en la tabla de la tarjeta Debito
		models.Model (Debito): es la instancia sobre la que se crea la tabla.

	Atributos de la clase: 
		Nro_Cuenta : Numero de cuenta.
		Nro_Tarjeta : Numero de tarjeta de debito.
		Tipo : Tipo de tarjeta de debido
		Nombre_Banco : Nombre del banco.
		Postiza : id del medio de pago
	"""
	Nro_Cuenta = models.CharField(primary_key=True, max_length = 20,validators = [RegexValidator(regex='[0-9]{20}', message='Nro cuenta incorrecto')])
	Nro_Tarjeta = models.CharField(max_length = 18,validators=[RegexValidator(regex='[0-9]{18}', message='Nro tarjeta incorrecto')])
	Tipo = models.CharField(max_length=9, validators=[tipo_debito_restr])
	Nombre_Banco = models.CharField(max_length=30)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		""" Devuelve los atributos de la clase """
		return [self.Nro_Cuenta,self.Nro_Tarjeta,self.Tipo,self.Nombre_Banco,self.Postiza]
	def __getallfieldNames__(self):
		""" Obtiene los nombres de los atributos de la clase"""
		return ["Nro_Cuenta","Nro_Tarjeta","Tipo","Nombre_Banco","Postiza"]
	def __gettablename__(self):
		""" Obtiene el nombre de la clase"""
		return "Debito"
	def __createElement__(self,parameters):
		""" Crea y retorna un nuevo nodo o elemento de la tabla"""
		return Debito(
				Nro_Cuenta = parameters["Nro_Cuenta"],
				Nro_Tarjeta = parameters["Nro_Tarjeta"],
				Tipo = parameters["Tipo"],
				Nombre_Banco = parameters["Nombre_Banco"],
				Postiza = parameters["Postiza"]
			)

class Credito(models.Model):
	""" Consiste en la tabla de la de tarjeta de Credito
		models.Model (Credito): es la instancia sobre la que se crea la tabla.

	Atributos de la clase: 
		Nro_Tarjeta : Numero de tarjeta de credito.
		Fecha_Vence : TFecha en que vence de tarjeta de credito
		Nombre_Banco : Nombre del banco.
		Postiza : id del medio de pago
	"""
	Nro_Tarjeta = models.CharField(primary_key=True,max_length = 18,validators=[RegexValidator(regex='[0-9]{18}', message='Nro tarjeta incorrecto')])
	Fecha_Vence = models.DateField() 
	Nombre_Banco = models.CharField(max_length=30)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		""" Devuelve los atributos de la clase """
		return [self.Nro_Tarjeta,self.Fecha_Vence,self.Nombre_Banco,self.Postiza]
	def __getallfieldNames__(self):
		""" Obtiene los nombres de los atributos de la clase"""
		return ["Nro_Tarjeta","Fecha_Vence","Nombre_Banco","Postiza"]
	def __gettablename__(self):
		""" Obtiene el nombre de la clase"""
		return "Credito"
	def __createElement__(self,parameters):
		""" Crea y retorna un nuevo nodo o elemento de la tabla"""
		return Credito(
				Nro_Tarjeta = parameters["Nro_Tarjeta"],
				Fecha_Vence = parameters["Fecha_Vence"],
				Nombre_Banco = parameters["Nombre_Banco"],
				Postiza = parameters["Postiza"]
			)

class Transferencia(models.Model):
	""" Consiste en la tabla de las transferencia
		models.Model (Transferencia): es la instancia sobre la que se crea la tabla.

	Atributos de la clase: 
		Nro_Referencia : Numero de referencia de la transferencia.
		Postiza : id del medio de pago
	"""
	Nro_Referencia = models.CharField(primary_key=True,max_length = 20, validators=[RegexValidator(regex='[0-9]{20}', message='Nro Referencia incorrecto')])
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		""" Devuelve los atributos de la clase """
		return [self.Nro_Referencia,self.Postiza]
	def __getallfieldNames__(self):
		""" Obtiene los nombres de los atributos de la clase"""
		return ["Nro_Referencia","Postiza"]
	def __gettablename__(self):
		""" Obtiene el nombre de la clase"""
		return "Transferencia"
	def __createElement__(self,parameters):
		""" Crea y retorna un nuevo nodo o elemento de la tabla"""
		return Debito(
				Nro_Referencia = parameters["Nro_Referencia"],
				Postiza = parameters["Postiza"]
			)

class Deposito(models.Model):
	""" Consiste en la tabla del deposito
		models.Model (Deposito): es la instancia sobre la que se crea la tabla.

	Atributos de la clase: 
		Referencia : Nro de referencia del deposito.
		Postiza : id del medio de pago
	"""
	Referencia = models.CharField(primary_key=True, max_length = 20, validators=[RegexValidator(regex='[0-9]{20}', message='Nro Referencia incorrecto')])
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		""" Devuelve los atributos de la clase """
		return [self.Referencia,self.Postiza]
	def __getallfieldNames__(self):
		""" Obtiene los nombres de los atributos de la clase"""
		return ["Referencia","Postiza"]
	def __gettablename__(self):
		""" Obtiene el nombre de la clase"""
		return "Deposito"
	def __createElement__(self,parameters):
		""" Crea y retorna un nuevo nodo o elemento de la tabla"""
		return Debito(
				Referencia = parameters["Referencia"],
				Postiza = parameters["Postiza"]
			)
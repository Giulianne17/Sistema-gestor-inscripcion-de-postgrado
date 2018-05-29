from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from django.apps import apps
from .models import *
from .forms import *

show_all_tables = True
element_actual = None

# Create your viewss here.
def index(request):
	if request.method=="POST":
		try:
			name=__getTableName__(request)
			__modififyDB__(name, __getParameters__(name,request),request)
			return  HttpResponseRedirect("/"+name)
		except:
			print("No se pudo modificar la BD")
			return  HttpResponseRedirect('/index')	
	else:
		if "coordinacion_" in request.path:
			return coordinacion(request)
		return __renderViewGET__(request)

def coordinacion(request):
	if request.method=="POST":
		try:
			name=__getTableName__(request)
			__modififyDB__(name, __getParameters__(name,request),request)
			return  HttpResponseRedirect("/"+name)
		except:
			print("No se pudo modificar la BD")
			return  HttpResponseRedirect('/index')	
	else:
		return __renderViewGET__(request)

def __renderViewGET__(request):
	newpath = __decideNewPath__(request.path)
	if request.path!="" and request.path!="/" and "index" not in request.path and "favicon" not in request.path:
		name = __getTableName__(request)
		return render(request, newpath, __getContext__(request,name,True))
	else:
		return render(request, newpath, __getContext__(request,"todas las Tablas",False))

def __renderViewPOST__(request):
	try:
		name = __getTableName__(request)
		__modififyDB__(name, __getParameters__(name,request),request)
		return  HttpResponseRedirect("/"+name)
	except:
		print("No se pudo modificar la BD")
		return  HttpResponseRedirect('/index')

def __getTableName__(request):
	if "coordinacion_" in request.path:
		return request.path.split("/")[1].split("_")[1]
	else:
		return request.path.split("/")[1]

def __decideNewPath__(stringPath):
	string = "crud/"
	if "coordinacion_" in stringPath:
		return string + "coordinacion.html"
	else:
		return string + "index.html"

def __getDBList__():
	all_tables = connection.introspection.table_names()
	tables_to_use = []
	for i in all_tables:
		if "InscripcionPostgrado" in i:
			tables_to_use.append(i.split("_",1)[1])
	return tables_to_use

def __getContext__(request, name, ismodel):
	if "coordinacion_" in request.path:
		return __buildContextAsignatura__(name)
	else:
		return __buildContext__(name,ismodel)
		
def __buildContext__(name,ismodel):
	if ismodel:
		model = apps.get_model(app_label='InscripcionPostgrado', model_name=name)
		column_list=model.__getallfieldNames__()
		table=model.objects.all()
		show_all_tables=False
	else:
		column_list=["Nombre de la tabla"]
		table=__getDBList__()
		show_all_tables=True
	context = {
			'table_name' : name,
			'table_column_list' : column_list,
			'table' : table,
			'show_all_tables' : show_all_tables
		}
	return context

def __buildContextAsignatura__(CodCoordinacion):
	model = apps.get_model(app_label='InscripcionPostgrado', model_name='asignatura')
	column_list = ["Cod_asignatura","Nombre_asig", "Creditos"]
	table = model.objects.filter(Cod_coordinacion = CodCoordinacion)
	show_all_tables = False
	temp = apps.get_model(app_label='InscripcionPostgrado', model_name='coordinacion')
	nameofcoordinacion = temp.objects.get(Cod_coordinacion = CodCoordinacion).Nombre_coordinacion
	context = {
			'table_name' : "asignaturas de " + nameofcoordinacion,
			'table_column_list' : column_list,
			'table' : table,
			'show_all_tables' : show_all_tables
		}
	return context

def __getParameters__(name,request):
	context=__buildContext__(name,True)
	parameters = { }
	for i in context["table_column_list"]:
		parameters[i]=request.POST.get(i)
	if "coordinacion_" in request.path:
		parameters["Cod_coordinacion"] = name
	return parameters

def __modififyDB__(name, parameters,request):
	if "coordinacion" in name:
		form=CoordinacionForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			raise
	elif "asignatura" in name:
		form = AsignaturaForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			raise
	elif "profesor" in name:
		form = ProfesorForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			raise
	elif "pertenece" in name:
		form = PerteneceForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			raise
	else:
		table = apps.get_model(app_label='InscripcionPostgrado', model_name=name)
		element=table.__createElement__(parameters)
		element.save()
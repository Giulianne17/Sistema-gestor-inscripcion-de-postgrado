from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from django.apps import apps
from .models import *
from .forms import *

show_all_tables = True
element_actual = None

# Create your views here.
def index(request):
	if request.method=="POST":
		try:
			name=request.path.split("/")[1]
			__modififyDB__(name, __getParameters__(name,request),request)
			return  HttpResponseRedirect("/"+name)
		except:
			print("No se pudo modificar la BD")
			return  HttpResponseRedirect('/index')
	else:
		if request.path!="" and request.path!="/" and "index" not in request.path and "favicon" not in request.path:
			name=request.path.split("/")[1]
			return render(request, 'crud/index.html', __buildContext__(name,True))
		else:
			return render(request, 'crud/index.html', __buildContext__("todas las Tablas",False))

def __getDBList__():
	all_tables = connection.introspection.table_names()
	tables_to_use = []
	for i in all_tables:
		if "InscripcionPostgrado" in i:
			tables_to_use.append(i.split("_",1)[1])
	return tables_to_use

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

def __getParameters__(name,request):
	context=__buildContext__(name,True)
	parameters = { }
	for i in context["table_column_list"]:
		parameters[i]=request.POST.get(i)
	return parameters

def __modififyDB__(name, parameters,request):
	if "coordinacion" in name:
		form=CoordinacionForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			raise
	elif "asignatura" in name:
		print(request.POST)
		form = AsignaturaForm(request.POST)
		print(form)
		if form.is_valid():
			form.save()
		else:
			form.save()
			print("no")
			raise
	else:
		table = apps.get_model(app_label='InscripcionPostgrado', model_name=name)
		element=table.__createElement__(parameters)
		element.save()
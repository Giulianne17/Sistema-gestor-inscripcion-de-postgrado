from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from django.apps import apps
from .models import *

show_all_tables = True
element_actual = None

# Create your views here.
def index(request):
	if request.method=="POST":
		#IMPLEMENTAR
		try:
			name=request.path.split("/")[1]
			context=_buildContext__(name,True)
			parameters = { }
			for i in context["column_list"]:
				parameters[i]=request.POST.get(i)
			__modififyDB__(context["table"], parameters)
			return  HttpResponseRedirect(name)
		except:
			print("No se pudo modificar la BD")
			return  HttpResponseRedirect('')
	else:
		if request.path!="" and request.path!="/" and "index" not in request.path:
			show_all_tables = False
			name=request.path.split("/")[1]
			return render(request, 'crud/index.html', __buildContext__(name,True))
		else:
			show_all_tables=True
			return render(request, 'crud/index.html', __buildContext__("All tables",False))

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
	else:
		column_list=["Nombre de la tabla"]
		table=__getDBList__()
	context = {
			'table_name' : name,
			'table_column_list' : column_list,
			'table' : table,
			'show_all_tables' : show_all_tables
		}
	return context

def __modififyDB__(table, parameters):
	element=table.__createElement__(parameters)
	element.save()
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from django.apps import apps
from .models import *
from .forms import *
from itertools import chain
from .render import *
import os
from django.contrib import messages
from .writeToFile import *

'''Atributo auxiliar que indica al template si se van a
mostrar todas las tablas existentes.'''
show_all_tables = True

def __redirectCenter__(request):
	'''Funcion que redirecciona a los views dependiendo del path
	solicitado.'''
	writeFilePath(request.path,"__redirectCenter__")
	if "coordinacion_" in request.path:
		return coordinacion(request)
	if "ofertas" in request.path:
		return ofertas(request)
	if "periodo" in request.path:
		return periodo(request)
	else:
		return index(request)

def index(request):
	'''Vista del index.
	Aqui se redirigen todos los request que no vayan a una
	coordinacion particular.	writeFilePath(request.path,"index")'''
	writeFilePath(request.path,"index")
	if request.method=="POST":
		return __renderViewPOST__(request,'/superuser','/')
	else:
		return __renderViewGET__(request)

# Vista de la coordinacion.
# Aqui se redirigen los request que van a una coordinacion en
# particular.
def coordinacion(request):
	writeFilePath(request.path,"coordinacion")
	if "delete" in request.path:
		return deleteAsignatura(request)
	if "edit" in request.path:
		return editAsignatura(request)
	if "orderby" in request.path:
		return orderbyAsignatura(request)
	if "search" in request.path:
		return searchAsignatura(request)
	if request.method=="POST":
		try:
			name = __getTableName__(request)
			__modififyDB__(name, __getParameters__(name,request),request)
			messages.info(request, 'Se ha agregado la asignatura de manera exitosa.')
			return  HttpResponseRedirect(request.path)
		except:
			print("No se pudo modificar la BD")
			form = AsignaturaForm(request.POST)
			form.fields['Cod_coordinacion'].widget = forms.HiddenInput()
			context = __buildContextAsignatura__(name)
			context['form'] = form
			return render(request, 'crud/coordinacion.html', context)
	else:
		return __renderViewGET__(request)

# Vista para borrar asignaturas
# Aqui llegan los request para borrar una entrada de la tabla de
# asignaturas de una coordinacion
def deleteAsignatura(request):
	writeFilePath(request.path,"deleteAsignatura")
	[path,codasig] = request.path.split("/delete_")
	table = apps.get_model(app_label='InscripcionPostgrado', model_name='asignatura')
	table.objects.filter(Cod_asignatura = codasig).delete()
	return  HttpResponseRedirect(path)

#Vista para editar asignaturas
# Aqui llegan los request para editar una asignatura.
# *Si es un POST:
# 		Ya el usuario ha enviado datos a traves del modal, se
# 		redirige a la funcion para el update.
# *Si es un GET:
#		El usuario ha hecho click en el edit de un elemento,
#		se debe renderizar el template pasando como contexto
#		el formulario para el elemento y un booleano para indicar
#		que se debe abrir el modal directamente.
def editAsignatura(request):
	writeFilePath(request.path,"editAsignatura")
	name = __getTableName__(request)
	cod = request.path.split('/edit_')[1]
	table = apps.get_model(app_label='InscripcionPostgrado', model_name='asignatura')
	element = table.objects.get(Cod_asignatura = cod)
	if request.method=="POST":
		element.delete()
		return updateAsignatura(request,element)
	else:
		context = __buildContextAsignatura__(name)
		context['editAsig'] = True
		form = AsignaturaForm(instance = element)
		form.fields['Cod_coordinacion'].widget = forms.HiddenInput()
		form.Cod_coordinacion = name
		context['form'] = form
		return render(request, 'crud/coordinacion.html', context)

# Vista para actualizar una asignatura.
def updateAsignatura(request,oldElement):
	writeFilePath(request.path,"updateAsignatura")
	name = request.path.split("/coordinacion_")[1].split("/")[0]
	[path,codasig] = request.path.split("/edit_")
	form = __returnForm__("",request)
	if form.is_valid():
		form.save()
		messages.info(request, 'Se ha modificado la asignatura de manera exitosa.')
		return HttpResponseRedirect(path)
	else:
		oldElement.Cod_asignatura = codasig
		oldElement.save()
		print("No se pudo modificar la BD")
		context = __buildContextAsignatura__(name)
		context['form'] = form
		return render(request, 'crud/coordinacion.html', context)

# Vista para buscar una asignatura dados unos parametros en el request
# *Si SearchInd esta en el path:
#		Esto indica que se esta interactuando con el modal de busqueda.
#		->Si es POST:
#			El modal de busqueda ha sido rellenado y debe redirigirse a
# 			la ruta de busqueda correspondiente.
# 		->Si es GET:
# 			Se quiere abrir el modal. Se renderiza el template con un booleano
# 			para indicar que debe abrise.		
# *En otros casos:
#		Se ha llegado por una ruta como "/search_attr=value". Filtra la tabla
#		completa de la coordinacion con estos datos y se le pasa al template.
def searchAsignatura(request):
	writeFilePath(request.path,"searchAsignatura")
	CodCoordinacion = __getTableName__(request)
	context = __buildContextAsignatura__(CodCoordinacion)
	if "/searchInd" in request.path:
		if request.method == "POST":
			attr = request.POST.get("attr")
			criterio = request.POST.get("criterio")
			if attr:
				return HttpResponseRedirect("/coordinacion_"+CodCoordinacion+"/search_"+attr+"="+criterio)
		else:
			context['searchAsig'] = True
			return render(request, 'crud/coordinacion.html', context)
	if request.method == "POST":
		try:
			name = __getTableName__(request)
			__modififyDB__(name, __getParameters__(name,request),request)
			messages.info(request, 'Se ha agregado la asignatura de manera exitosa.')
			return  HttpResponseRedirect(request.path)
		except:
			print("No se pudo modificar la BD")
			form = AsignaturaForm(request.POST)
			form.fields['Cod_coordinacion'].widget = forms.HiddenInput()
			context = __buildContextAsignatura__(name)
			context['form'] = form
			return render(request, 'crud/coordinacion.html', context)
	context = __returnContextWithSearchTable__(request.path,context)
	context['searchBool'] = True
	context['backPath'] = request.path.split("/search_")[0]
	return render(request, 'crud/coordinacion.html', context)

# Funcion que retorna la tabla dado un criterio de busqueda
def __returnContextWithSearchTable__(currentpath,context):
	writeFilePath(request.path,"__returnContextWithSearchTable__")
	[path,searchparam] = currentpath.split("/search_")
	searchparam = searchparam.split("/")[0]
	[attrb,givenSearch] = searchparam.split("=")
	if "Cod_asig" in attrb:
		context['table'] = context['table'].filter(Cod_asignatura__icontains=givenSearch)
	elif "Nombre_asig" in attrb:
		context['table'] = context['table'].filter(Nombre_asig__icontains=givenSearch)
	return context

# Vista para ordenar las asignaturas segun corresponda.
# *Si orderbyInd esta en el path:
#		Esto indica que se esta interactuando con el modal de orderby.
#		->Si es POST:
#			El modal de orderby ha sido rellenado y debe redirigirse a
# 			la ruta de orderby correspondiente.
# 		->Si es GET:
# 			Se quiere abrir el modal. Se renderiza el template con un booleano
# 			para indicar que debe abrise.		
# *En otros casos:
#		Se ha llegado por una ruta como "/orderby_attr". Filtra la tabla completa
#		de la coordinacion con estos datos y se le pasa al template.
def orderbyAsignatura(request):
	writeFilePath(request.path,"orderbyAsignatura")
	if request.method == "POST":
		try:
			name = __getTableName__(request)
			__modififyDB__(name, __getParameters__(name,request),request)
			messages.info(request, 'Se ha agregado la asignatura de manera exitosa.')
			return  HttpResponseRedirect(request.path)
		except:
			print("No se pudo modificar la BD")
			form = AsignaturaForm(request.POST)
			form.fields['Cod_coordinacion'].widget = forms.HiddenInput()
			context = __buildContextAsignatura__(name)
			context['form'] = form
			return render(request, 'crud/coordinacion.html', context)
	CodCoordinacion = __getTableName__(request)
	context = __buildContextAsignatura__(CodCoordinacion)
	[path,orderparam] = request.path.split("/orderby_")
	[attr,style] = orderparam.split("=")
	if "search_" in request.path:
		context = __returnContextWithSearchTable__(request.path,context)
	if "desc" in style:
		context['table'] = context['table'].order_by("-"+attr)
	elif "asc" in style:
		context['table'] = context['table'].order_by(attr)
	context['backPath'] = path
	return render(request, 'crud/coordinacion.html', context)

def periodo(request):
	''' Vista de periodo de oferta.
	Aqui se redirigen todos los request que van al path /periodos, y desde aquí se
	vuelve a redirigir a todas las funcionalidades correspondientes, según la ruta
	del path.
	'''
	writeFilePath(request.path,"periodo")
	if "delete" in request.path:
		return deletePeriodo(request)
	if "edit" in request.path:
		return editPeriodo(request)
	if "orderby" in request.path:
		return orderbyPeriodo(request)
	if "search" in request.path:
		return searchPeriodo(request)
	if "printPdf" in request.path:
		# Se consigue el contexto de acuerdo a la tabla
		context = __buildContext__("Trimestre",True)
		# El siguiente bloque consigue todas las periodos de oferta, ordenados de
		# de manera ascendente según el periodo
		values = context['table'].values_list('Anio',flat=True).order_by('Anio').distinct()
		table = None
		for i in values:
			table=__appendAnioOrderedByPeriodo__("asc",i,context['table'],table)
		# Se axtualiza la tabla en el contexto
		context['table'] = table
		# El siguiente bloque de codigo consigue todas las asignaturas de las
		# ofertas conseguidas arriba, en el mismo orden en que aparecen dichos
		# periodos en la tabla
		tableOfertas = apps.get_model(app_label='InscripcionPostgrado', model_name='Se_ofrece')
		tablesList = []
		if context['table']!=None:
			for i in context['table']:
				tablesList.append(tableOfertas.objects.filter(Periodo__id = i.id))
		# Se actualiza la lista de querys en el contexto
		context['table'] = tablesList
		# Se actualizan las columnas a mostrar en el pdf
		context['table_column_list'] = ["Código", "U.C","Denominación","Profesor","Programa","Horario","Periodo"]
		return printPdf(request,"TODAS LAS ASIGNATURAS OFERTADAS EN TODOS LOS PERIODOS DISPONIBLES",context)
	if request.method=="POST":
		try:
			__modififyDB__("Trimestre", None,request)
			messages.info(request, 'Se ha agregado la oferta de manera exitosa.')
			return  HttpResponseRedirect(request.path)
		except:
			print("No se pudo modificar la BD")
			context = __buildContext__("Trimestre",True)
			context ["table_column_list"] = ["Periodo","Año","Operaciones"]
			context ["backpath"] = ""
			context["form"] = __returnForm__("Trimestre",request)
			return render(request, 'crud/periodo.html', context)
	else:
		context = __buildContext__("Trimestre",True)
		context ["backpath"] = ""
		context["form"] = __returnForm__("Trimestre",request)
		context ["table_column_list"] = ["Periodo","Año","Operaciones"]
		return render(request, 'crud/periodo.html', context)

def printPdf(request,givenFilter,context):
	
	''' Funcion que dado un request identifica desde donde ha llegado (puede llegar)
	desde /periodos o desde /ofertas_X con X entero, para renderizar el pdf
	correspondiente
	'''
	writeFilePath(request.path,"printPdf")
	context['givenFilter'] = givenFilter
	context['os'] = os
	if "periodo" in request.path:
		if len(context['table'])>1:
			context['isPeriodoList'] = True
		elif len(context['table'])==1:
			context['table']=context['table'][0]
			context['table_column_list'] = ["Código", "U.C","Denominación","Profesor","Programa","Horario"]
		else:
			context['isPeriodoList'] = True
			context['isEmpty'] = True
	return render_to_pdf('crud/pdfTemplate.html',context)

def deletePeriodo(request):
	''' Función que borra un periodo.
	Dado un request, consigue el elemento desde la tabla correspondiente y lo
	elimina
	'''
	writeFilePath(request.path,"deletePeriodo")
	[path,Id] = request.path.split("/delete_")
	table = apps.get_model(app_label='InscripcionPostgrado', model_name='Trimestre')
	table.objects.filter(id = Id).delete()
	return  HttpResponseRedirect(path)

def editPeriodo(request):
	''' Función que maneja las modificaciones de elementos en la tabla de periodos de
	oferta. Trabaja de la siguiente manera:
	
	* Si el método del request es GET ->
			Se tiene que abrir el modal de modificación con los datos del elemento
		cargados. Se consigue el elemento desde la tabla según su id, y posteriormente
		se instancia el form de ese elemento para retornarlo en el contexto.
			Además, se envía un booleano editOferta para que el template abra el modal
		correspondiente
	
	* Si el método del request es POST ->
			Se ha modificado el form, y es necesario verificar si es válido. Se consigue
		la tabla de asignaturas ofertadas para ese periodo, y se redirige el request
		junto con esta tabla a la función updatePeriodo
	'''
	writeFilePath(request.path,"editPeriodo")
	cod = request.path.split('/edit_')[1]
	table = apps.get_model(app_label='InscripcionPostgrado', model_name='Trimestre')
	element = table.objects.get(id = cod)
	if request.method=="POST":
		asignaturasOfertadas = apps.get_model(app_label='InscripcionPostgrado', model_name='Se_ofrece').objects.filter(Periodo=element.id)
		return updatePeriodo(request,element,asignaturasOfertadas)
	else:
		context = __buildContext__("Trimestre",True)
		context['editOferta'] = True
		form = TrimestreForm(instance=element)
		context['form'] = form
		context ["table_column_list"] = ["Periodo","Año","Operaciones"]
		context ["backpath"] = "periodos"
		return render(request, 'crud/periodo.html', context)

def updatePeriodo(request,oldElement,asignaturasOfertadas):
	''' Función que maneja las modificaciones y el update de elementos en la tabla de
	periodos de	oferta, cuando el usuario ha hecho click en salvar en el modal.
	
	Consigue el form a partir de lo recuperado desde el POST, y procede como sigue:
	
	* Si el form es válido ->
			Se guarda el elemento como un nuevo elemento, y se proceden a conseguir
		todos las asignaturas ofertadas en el viejo periodo son actualizadas con la
		referencia al nuevo.
	
	* Si el form no es válido ->
			Se retorna el form para que los errores aparezcan en el template.
	'''
	writeFilePath(request.path,"updatePeriodo")
	[path,ID] = request.path.split("/edit_")
	form = __returnForm__("Trimestre",request)
	if form.is_valid():
		form.save()
		table = apps.get_model(app_label='InscripcionPostgrado', model_name='Trimestre')
		element = table.objects.get(Periodo = form['Periodo'].value(),Anio=form['Anio'].value())
		asignaturasOfertadas.update(Periodo=element.id)
		oldElement.delete()
		messages.info(request, 'Se ha modificado la oferta de manera exitosa.')
		return HttpResponseRedirect(path)
	else:
		print("No se pudo modificar la BD")
		context = __buildContext__("Trimestre",True)
		context ["table_column_list"] = ["Periodo","Año","Operaciones"]
		context ["backpath"] = "periodos"
		context["form"] = __returnForm__("Trimestre",request)
		return render(request, 'crud/periodo.html', context)

def searchPeriodo(request):
	''' Función que maneja las búsquedas sobre las ofertas en la tabla.

	Existen diferentes formas de trabajo de esta función:

	* Si "/searchInd" está en el path:
			Se refiere a que se está trabajando con el modal de búsqueda. A su vez, hay dos
		opciones:

		** Si el método del request es GET -> 
				El usuario ha hecho click en el botón Buscar del template, se debe abrir
			el modal. Para ello, se carga el contexto junto con un booleano searchOferta
			seteado en True.

		** Si el método del request es POST ->
				Se han introducido criterios de búsqueda. Se recuperan del template
			y se redirige al path con los mismos.
	
	* Si "/searchInd" no está en el path:
			Se está llegando desde un path con los criterios de búsqueda. Se consigue el
		contexto según los mismos.

		** Si el método del request es GET -> 
				Se envia la tabla correspondiente al template para ser mostrada.

		** Si el método del request es POST ->
				Luego de realizar una búsqueda, el usuario quiere agregar un elemento a
			la tabla general. Se consiguen los datos y se modifica la tabla si son válidos,
			de lo contrario envía el form con los errores al mismo path.

	Además, se agrega una funcionalidad:

	* Si "printPdf" está en path:
			Se quiere imprimir las asignaturas ofertadas en los periodos que aparecieron en la
		búsqueda. Se consigue la tabla, se ordena según el periodo, y luego se hace el query
		en la tabla se_ofrece para conseguir las asignaturas y mandarlas a la función que
		imprime el pdf.
	'''
	writeFilePath(request.path,"searchPeriodo")
	context = __buildContext__("Trimestre",True)
	if "/searchInd" in request.path:
		if request.method == "POST":
			criterio = request.POST.get("criterio")
			if criterio:
				return HttpResponseRedirect("/periodos/search="+criterio)
		else:
			context['searchOferta'] = True
			context ["table_column_list"] = ["Periodo","Año","Operaciones"]
			context ["backpath"] = "periodos"
			context["form"] = __returnForm__("Trimestre",request)
			return render(request, 'crud/periodo.html', context)
	if request.method == "POST":
		try:
			__modififyDB__("Trimestre", None,request)
			messages.info(request, 'Se ha agregado la oferta de manera exitosa.')
			return  HttpResponseRedirect(request.path)
		except:
			print("No se pudo modificar la BD")
			context ["table_column_list"] = ["Periodo","Año","Operaciones"]
			context ["backpath"] = request.path.split("/search=")[0]
			context["form"] = __returnForm__("Trimestre",request)
			return render(request, 'crud/periodo.html', context)
	context = __returnContextPeriodoWithSearchTable__(request.path,context)
	if "printPdf" in request.path:
		givenSearch = request.path.split("/search=")[1].split("/")[0]
		values = context['table'].values_list('Anio',flat=True).order_by('Anio').distinct()
		table = None
		for i in values:
			table=__appendAnioOrderedByPeriodo__("asc",i,context['table'],table)
		context['table'] = table
		tableOfertas = apps.get_model(app_label='InscripcionPostgrado', model_name='Se_ofrece')
		tablesList = []
		if context['table']!=None:
			for i in context['table']:
				tablesList.append(tableOfertas.objects.filter(Periodo__id = i.id))
		context['table'] = tablesList
		context['table_column_list'] = ["Código", "U.C","Denominación","Profesor","Programa","Horario","Periodo"]
		return printPdf(request,"Resultados de la busqueda: \""+givenSearch+"\"",context)
	context['searchBool'] = True
	context['backpath'] = request.path.split("/search=")[0]
	context["table_column_list"] = ["Periodo","Año","Operaciones"]
	context["form"] = __returnForm__("Trimestre",request)
	return render(request, 'crud/periodo.html', context)

def __returnContextPeriodoWithSearchTable__(currentpath,context):
	''' Función que dado un path de búsqueda, retorna el contexto de ese path junto con la
	tabla de búsqueda correspondiente a los criterios dados en el path.
	'''
	[path,searchparam] = currentpath.split("/search=")
	searchparam = searchparam.split("/")[0].split(" ")
	table1 = None
	anios = []
	for criterio in searchparam:
		if criterio[0] in "0123456789":
			try:
				assert(isinstance(int(criterio),int))
				anios.append(criterio)
			except:
				pass
		else:
			for i in ['ENE-MAR', 'ABR-JUL','VERANO','SEPT-DIC','ENERO-MARZO','ABRIL-JULIO','SEPTIEMBRE-DICIEMBRE']:
				if criterio.lower() in i.lower():
					if i=='ENE-MAR' or i=='ENERO-MARZO':
						periodo="EM"
					elif i=='ABR-JUL' or i =='ABRIL-JULIO':
						periodo="AJ"
					elif i=='VERANO':
						periodo="V"
					elif i=='SEPT-DIC' or i=='SEPTIEMBRE-DICIEMBRE':
						periodo="SD"
					if table1==None:
						table1=context['table'].filter(Periodo__icontains=periodo)
					else:
						table1=table1 | context['table'].filter(Periodo__icontains=periodo)
					break
	if len(anios)>0:
		if table1==None:
			table1 = context['table'].filter(Anio__icontains=anios[0])
		else:
			table1 = table1.filter(Anio__icontains=anios[0])
	context['table'] = table1
	return context

def orderbyPeriodo(request):
	''' Función que maneja las búsquedas sobre las ofertas en la tabla.

	Existen diferentes formas de trabajo de esta función:

	* Si el método del request es GET -> 
			Aquí, se ve si se está ordenando una tabla con criterios de búsqueda,
		en cuyo caso se consigue la tabla de búsqueda y luego se ordena.
		Además:
			* Si "printPdf" está en path:
					Se quiere imprimir las asignaturas ofertadas en los periodos que aparecieron en la
				búsqueda. Se consigue la tabla, se ordena según el periodo, y luego se hace el query
				en la tabla se_ofrece para conseguir las asignaturas y mandarlas a la función que
				imprime el pdf.

	* Si el método del request es POST ->
			Luego de ordenar una tabla, el usuario quiere agregar un elemento a
		la tabla general. Se consiguen los datos y se modifica la tabla si son válidos,
		de lo contrario envía el form con los errores al mismo path.
	'''
	context = __buildContext__("Trimestre",True)
	[path,orderparam] = request.path.split("/orderby_")
	if request.method == "POST":
		try:
			__modififyDB__("Trimestre", None,request)
			messages.info(request, 'Se ha agregado la oferta de manera exitosa.')
			return  HttpResponseRedirect(request.path)
		except:
			print("No se pudo modificar la BD")
			context ["table_column_list"] = ["Periodo","Año","Operaciones"]
			context ["backpath"] = path
			context["form"] = __returnForm__("Trimestre",request)
			return render(request, 'crud/periodo.html', context)
	[attr,style] = orderparam.split("=")
	if "asc" in style:
		styleaux = "ascendente"
	else:
		styleaux = "descendente"
	if "search=" in request.path:
		context = __returnContextPeriodoWithSearchTable__(request.path,context)
	if "Periodo" in attr:
		aux = "ordenando el periodo alfabéticamente"
		if "desc" in style:
			context['table'] = context['table'].order_by("-"+attr)
		elif "asc" in style:
			context['table'] = context['table'].order_by(attr)
	else:
		aux = "ordenado por periodo"
		table = None
		if "desc" in style:
			values = context['table'].values_list('Anio',flat=True).order_by('-Anio').distinct()
			for i in values:
				table=__appendAnioOrderedByPeriodo__(style,i,context['table'],table)
		elif "asc" in style:
			values = context['table'].values_list('Anio',flat=True).order_by('Anio').distinct()
			for i in values:
				table=__appendAnioOrderedByPeriodo__(style,i,context['table'],table)
		context['table'] = table
	context ["table_column_list"] = ["Periodo","Año","Operaciones"]
	context ["backpath"] = path
	context["form"] = __returnForm__("Trimestre",request)
	if "printPdf" in request.path:
		tableOfertas = apps.get_model(app_label='InscripcionPostgrado', model_name='Se_ofrece')
		tablesList = []
		if context['table']!=None:
			for i in context['table']:
				tablesList.append(tableOfertas.objects.filter(Periodo__id = i.id))
		context['table'] = tablesList
		context['table_column_list'] = ["Código", "U.C","Denominación","Profesor","Programa","Horario","Periodo"]
		if "search" in request.path:
			givenSearch = request.path.split("/search=")[1].split("/")[0]
			return printPdf(request,"Resultados de la busqueda: \"" + givenSearch + "\", "+aux+" de manera "+styleaux,context)
		else:
			return printPdf(request,"TODAS LAS OFERTAS, "+aux+" de manera "+styleaux,context)
	return render(request, 'crud/periodo.html', context)

def __appendAnioOrderedByPeriodo__(style,year,majorTable,outputTable):
	''' Función que dado un style (ascendente o descendente), consigue todos los periodos dentro de
	un año dado, ordenados según su trimestre.
	'''
	tableAnio = majorTable.filter(Anio=year)
	tableEM = tableAnio.filter(Periodo="EM")
	tableAJ = tableAnio.filter(Periodo="AJ")
	tableV = tableAnio.filter(Periodo="V")
	tableSD = tableAnio.filter(Periodo="SD")
	if "asc" in style:
		result = chain(tableEM,tableAJ,tableV,tableSD)
	else:
		result = chain(tableSD,tableV,tableAJ,tableEM)
	if outputTable==None:
		return result
	else:
		return chain(outputTable,result)

def ofertas(request):
	''' Vista de asignaturas ofertadas.
	Aqui se redirigen todos los request que van al path /ofertas_X con X entero, y desde aquí
	se vuelve a redirigir a todas las funcionalidades correspondientes, según la ruta del
	path.
	'''
	if "delete" in request.path:
		return deleteOferta(request)
	if "edit" in request.path:
		return editOferta(request)
	if "orderby" in request.path:
		return orderbyOferta(request)
	if "search" in request.path:
		return searchOferta(request)
	if "printPdf" in request.path:
		context = __buildContextOferta__(request)
		cod = request.path.split("/ofertas_")[1].split("/")[0]
		element = apps.get_model(app_label='InscripcionPostgrado', model_name='trimestre').objects.get(id=cod)
		return printPdf(request,element.returnTrimWithAnio(),context)
	if request.method =="POST":
		try:
			__modififyDB__("", None,request)
			messages.info(request, 'Se ha agregado la asignatura a la oferta de manera exitosa.')
			return  HttpResponseRedirect(request.path)
		except:
			print("No se pudo modificar la BD")
			context = __getContext__(request,"",False)
			return render(request, 'crud/oferta.html', context)
	else:
		context = __getContext__(request,"",False)
		return render(request, 'crud/oferta.html', context)

def deleteOferta(request):
	''' Función que borra una asignatura de una oferta.
	Dado un request, consigue el elemento desde la tabla correspondiente y lo
	elimina
	'''
	[path,Id] = request.path.split("/delete_")
	table = apps.get_model(app_label='InscripcionPostgrado', model_name='se_ofrece')
	table.objects.filter(id = Id).delete()
	return  HttpResponseRedirect(path)

def editOferta(request):
	''' Función que maneja las modificaciones de elementos en la tabla de asignaturas de
	la oferta. Trabaja de la siguiente manera:
	
	* Si el método del request es GET ->
			Se tiene que abrir el modal de modificación con los datos del elemento
		cargados. Se consigue el elemento desde la tabla según su id, y posteriormente
		se instancia el form de ese elemento para retornarlo en el contexto.
			Además, se envía un booleano editOferta para que el template abra el modal
		correspondiente.
	
	* Si el método del request es POST ->
			Se ha modificado el form, y es necesario verificar si es válido. Se consigue
		la tabla de asignaturas ofertadas para ese periodo, y se redirige el request
		junto con esta tabla a la función updatePeriodo
	'''
	cod = request.path.split('/edit_')[1]
	table = apps.get_model(app_label='InscripcionPostgrado', model_name='se_ofrece')
	element = table.objects.get(id = cod)
	if request.method=="POST":
		element.delete()
		return updateOferta(request,element)
	else:
		context = __buildContextOferta__(request)
		context['editOferta'] = True
		form = Se_OfreceForm(instance = element)
		form.fields['Periodo'].widget = forms.HiddenInput()
		context['form'] = form
		return render(request, 'crud/oferta.html', context)

def updateOferta(request,oldElement):
	''' Función que maneja las modificaciones y el update de elementos en la tabla de
	asignaturas de la oferta, cuando el usuario ha hecho click en salvar en el modal.
	
	Consigue el form a partir de lo recuperado desde el POST, y procede como sigue:
	
	* Si el form es válido ->
			Se guarda el elemento como un nuevo elemento, y se redirige al path de la tabla
		de asignaturas de ofertas.
	
	* Si el form no es válido ->
			Se guarda el elemento viejo y se retorna el form para que los errores
		aparezcan en el template.
	'''
	[path,ID] = request.path.split("/edit_")
	form = __returnForm__("",request)
	if form.is_valid():
		form.save()
		messages.info(request, 'Se ha modificado la oferta de la asignatura de manera exitosa.')
		return HttpResponseRedirect(path)
	else:
		oldElement.id = ID
		oldElement.save()
		print("No se pudo modificar la BD")
		context = __buildContextOferta__(request)
		context['form'] = form
		return render(request, 'crud/oferta.html', context)

def searchOferta(request):
	''' Función que maneja las búsquedas sobre las asignaturas ofertadas en la tabla.

	Existen diferentes formas de trabajo de esta función:

	* Si "/searchInd" está en el path:
			Se refiere a que se está trabajando con el modal de búsqueda. A su vez, hay dos
		opciones:

		** Si el método del request es GET -> 
				El usuario ha hecho click en el botón Buscar del template, se debe abrir
			el modal. Para ello, se carga el contexto junto con un booleano searchOferta
			seteado en True.

		** Si el método del request es POST ->
				Se han introducido criterios de búsqueda. Se recuperan del template
			y se redirige al path con los mismos.
	
	* Si "/searchInd" no está en el path:
			Se está llegando desde un path con los criterios de búsqueda. Se consigue el
		contexto según los mismos.

		** Si el método del request es GET -> 
				Se envia la tabla correspondiente al template para ser mostrada.

		** Si el método del request es POST ->
				Luego de realizar una búsqueda, el usuario quiere agregar un elemento a
			la tabla general. Se consiguen los datos y se modifica la tabla si son válidos,
			de lo contrario envía el form con los errores al mismo path.

	Además, se agrega una funcionalidad:

	* Si "printPdf" está en path:
			Se quiere imprimir las asignaturas ofertadas en los periodos que aparecieron en la
		búsqueda. Se consigue la tabla, y se manda a la función que imprime el pdf.
	'''
	context = __buildContextOferta__(request)
	if "/searchInd" in request.path:
		if request.method == "POST":
			attr = request.POST.get("attr")
			criterio = request.POST.get("criterio")
			cod = request.path.split("/ofertas_")[1].split("/")[0]
			if attr:
				return HttpResponseRedirect("/ofertas_"+cod+"/search_"+attr+"="+criterio)
		else:
			context['searchOferta'] = True
			return render(request, 'crud/oferta.html', context)
	if request.method == "POST":
		try:
			__modififyDB__("", None,request)
			messages.info(request, 'Se ha agregado la asignatura a la oferta de manera exitosa.')
			return  HttpResponseRedirect(request.path)
		except:
			print("No se pudo modificar la BD")
			context = __getContext__(request,"",False)
			return render(request, 'crud/oferta.html', context)
	context = __returnContextOfertaWithSearchTable__(request.path,context)
	if "printPdf" in request.path:
		[attrb,givenSearch] = request.path.split("/search_")[1].split("/")[0].split("=")
		if "Cod_asig" in attrb:
			attr = "Codigo de asignatura"
		elif "Nombre_asig" in attrb:
			attr = "Nombre de asignatura"
		elif "Prof" in attrb:
			attr = "Profesor"
		cod = request.path.split("/ofertas_")[1].split("/")[0]
		element = apps.get_model(app_label='InscripcionPostgrado', model_name='trimestre').objects.get(id=cod)
		return printPdf(request,element.returnTrimWithAnio()+". Resultados de la busqueda: "+attrb+" = \""+givenSearch+"\"",context)
	context['searchBool'] = True
	context['backPath'] = request.path.split("/search_")[0]
	return render(request, 'crud/oferta.html', context)

def __returnContextOfertaWithSearchTable__(currentpath,context):
	''' Función que dado un path de búsqueda, retorna el contexto de ese path junto con la
	tabla de búsqueda correspondiente a los criterios dados en el path.
	'''
	[path,searchparam] = currentpath.split("/search_")
	searchparam = searchparam.split("/")[0]
	[attrb,givenSearch] = searchparam.split("=")
	if "Cod_asig" in attrb:
		context['table'] = context['table'].filter(Cod_asignatura__Cod_asignatura__icontains=givenSearch)
	elif "Nombre_asig" in attrb:
		context['table'] = context['table'].filter(Cod_asignatura__Nombre_asig__icontains=givenSearch)
	elif "Prof" in attrb:
		table1 = context['table'].filter(Id_prof__Nombres__icontains=givenSearch)
		table2 = context['table'].filter(Id_prof__Apellidos__icontains=givenSearch)
		context['table'] = table1 | table2
	elif "Horario" in attrb:
		table1 = context['table'].filter(Horario__icontains=givenSearch)
		table2 = context['table'].filter(Dia__icontains=givenSearch)
		context['table'] = table1 | table2
	elif "Periodo" in attrb:
		table1 = None
		for i in ['ENE-MAR', 'ABR-JUL','VERANO','SEPT-DIC']:
			if givenSearch.lower() in i.lower():
				if i=='ENE-MAR':
					periodo="EM"
				elif i=='ABR-JUL':
					periodo="AJ"
				elif i=='VERANO':
					periodo="V"
				elif i=='SEPT-DIC':
					periodo="SD"
				if table1==None:
					table1=context['table'].filter(Periodo__icontains=periodo)
				else:
					table1=table1 | context['table'].filter(Periodo__icontains=periodo)
		table2 = context['table'].filter(Anio__icontains=givenSearch)
		if table1==None:
			context['table'] = table2
		else:
			context['table'] = table1 | table2
	return context

def orderbyOferta(request):
	''' Función que maneja las búsquedas sobre las ofertas en la tabla.

	Existen diferentes formas de trabajo de esta función:

	* Si el método del request es GET -> 
			Aquí, se ve si se está ordenando una tabla con criterios de búsqueda,
		en cuyo caso se consigue la tabla de búsqueda y luego se ordena.
		Además:
			* Si "printPdf" está en path:
					Se quiere imprimir las asignaturas ofertadas en los periodos que aparecieron en la
				búsqueda. Se consigue la tabla para mandarla a la función que	imprime el pdf.

	* Si el método del request es POST ->
			Luego de ordenar una tabla, el usuario quiere agregar un elemento a
		la tabla general. Se consiguen los datos y se modifica la tabla si son válidos,
		de lo contrario envía el form con los errores al mismo path.
	'''
	if request.method == "POST":
		try:
			__modififyDB__("", None,request)
			messages.info(request, 'Se ha agregado la asignatura a la oferta de manera exitosa.')
			return  HttpResponseRedirect(request.path)
		except:
			print("No se pudo modificar la BD")
	context = __buildContextOferta__(request)
	[path,orderparam] = request.path.split("/orderby_")
	[attr,style] = orderparam.split("=")
	if "asc" in style:
		styleaux = "ascendente"
	else:
		styleaux = "descendente"
	if "search_" in request.path:
		context = __returnContextOfertaWithSearchTable__(request.path,context)
	if "Nombre_asig" in attr:
		attr = "Cod_asignatura__" + attr
		aux = "Nombre de asignatura"
	if "Fecha" not in attr:
		if "Nombre_asig" not in attr:
			aux = "Codigo de asignatura"
		if "desc" in style:
			context['table'] = context['table'].order_by("-"+attr)
		elif "asc" in style:
			context['table'] = context['table'].order_by(attr)
	else:
		aux = "Periodo"
		table = None
		if "desc" in style:
			values = context['table'].values_list('Anio',flat=True).order_by('-Anio').distinct()
			for i in values:
				table=__appendAnioOrderedByPeriodo__(style,i,context['table'],table)
		elif "asc" in style:
			values = context['table'].values_list('Anio',flat=True).order_by('Anio').distinct()
			for i in values:
				table=__appendAnioOrderedByPeriodo__(style,i,context['table'],table)
		context['table'] = table
	context['backPath'] = path
	if "printPdf" in request.path:
		cod = request.path.split("/ofertas_")[1].split("/")[0]
		element = apps.get_model(app_label='InscripcionPostgrado', model_name='trimestre').objects.get(id=cod)
		if "search_" in request.path:
			[attrb,givenSearch] = request.path.split("/search_")[1].split("/")[0].split("=")
			if "Cod_asig" in attrb:
				attr = "Codigo de asignatura"
			elif "Nombre_asig" in attrb:
				attr = "Nombre de asignatura"
			elif "Prof" in attrb:
				attr = "Profesor"
			return printPdf(request,element.returnTrimWithAnio()+". Resultados de la busqueda: "+attr+" = \""+givenSearch + "\", ordenado por "+aux+" de manera "+styleaux,context)
		else:
			return printPdf(request,element.returnTrimWithAnio()+", ordenado por "+aux+" de manera "+styleaux,context)
	return render(request, 'crud/oferta.html', context)


def __renderViewGET__(request):
	''' Funcion que renderiza un template de un GET request
	'''
	newpath = __decideNewPath__(request.path)
	if request.path!="" and request.path!="/" and "index" not in request.path and "favicon" not in request.path:
		if "/superuser" in request.path:
			return render(request, newpath, __getContext__(request,"todas las Tablas",False))
		else:
			name = __getTableName__(request)
			context = __getContext__(request,name,True)
			form = __returnForm__(name,request)
			context["form"] = form
			return render(request, newpath, context)
	else:
		name="Inicio"
		return render(request, 'crud/inicio.html', None)

def __renderViewPOST__(request,initialpath,auxpath):
	""" 	Funcion que renderiza un template de un POST request.
	Toma dos path que se utilizan según el caso
		* initialpath	= 	La base de datos no pudo ser modificada
		* auxpath		=	La base de datos fue modificada  """
	try:
		name = __getTableName__(request)
		__modififyDB__(name, __getParameters__(name,request),request)
		messages.info(request, 'Se ha agregado el elemento a la tabla de manera exitosa.')
		return  HttpResponseRedirect(auxpath+name)
	except:
		print("No se pudo modificar la BD")
		form = __returnForm__(name,request)
		if "index" in request.path or "coordinacion" in request.path or "/"==request.path:
			context = __buildContext__("coordinacion",True)
		else:
			context = __buildContext__(name,True)
		if form != None:
			context['form'] = form
		return render(request, 'crud/index.html', context)

def __getTableName__(request):
	""" 	Funcion que consigue un string dependiendo del caso:
	* Si se esta en una coordinacion:
			El nombre que retorna es el codigo de la coordinacion
	* En el resto de los casos:
			Retorna el nombre de la tabla que indica el path """
	if "coordinacion_" in request.path:
		return request.path.split("/")[1].split("_")[1]
	else:
		if "favicon" in request.path or "/"==request.path or "index" in request.path:
			return "coordinacion"
		else:
			return request.path.split("/")[1]


def __decideNewPath__(stringPath):
	""" Funcion que dado la ruta actual retorna la ruta del template
	que debe renderizarse. """
	string = "crud/"
	if "coordinacion_" in stringPath:
		return string + "coordinacion.html"
	else:
		return string + "index.html"

# Funcion que retorna una lista con todas las tablas disponibles
# en la BD
def __getDBList__():
	all_tables = connection.introspection.table_names()
	tables_to_use = []
	for i in all_tables:
		if "InscripcionPostgrado" in i:
			tables_to_use.append(i.split("_",1)[1])
	return tables_to_use

# Funcion que retorna el contexto que se va a pasar al render
# dado el caso:
# * Si se esta haciendo el request desde una coordinacion:
#		Se busca mostrar asignaturas de esa coordinacion.
#		Redireccionar a la funcion que filtra por su codigo.
#		ismodel no es utilizado en este caso.
# * En otros casos:
#		El request se esta haciendo desde cualquier otra tabla.
#		En este caso, se pasa a la funcion correspondiente.
#		Se requiere ismodel como parametro para la misma.
def __getContext__(request, name, ismodel):
	if "coordinacion_" in request.path:
		return __buildContextAsignatura__(name)
	elif "ofertas" in request.path:
		return __buildContextOferta__(request)
	else:
		return __buildContext__(name,ismodel)

# Funcion que retorna el contexto que se va a pasar al render
# dado el caso:
# * Si ismodel == True:
#		Esto indica que se quiere mostrar una tabla (modelo)
#		en particular. Se busca el modelo por medio de name
#		y se consiguen todos los elementos de la misma.
# * En otros casos:
#		Se quiere mostrar todas las tablas existentes, no un
#		solo modelo. Se consigue una lista de todas las tablas
#		existentes por otra funcion.
def __buildContext__(name,ismodel):
	if ismodel:
		model = apps.get_model(app_label='InscripcionPostgrado', model_name=name)
		column_list=model.__getallfieldNames__(model)
		table=model.objects.all()
		show_all_tables=False
	else:
		column_list=["Nombre de la tabla"]
		table=__getDBList__()
		show_all_tables=True
	return __contextTemplate__(name,column_list,table,show_all_tables,None)

# Funcion que dado el Codigo de una coordinacion retorna el
# contexto para el template con solo las asignaturas de dicha
# coordinacion.
def __buildContextAsignatura__(CodCoordinacion):
	model = apps.get_model(app_label='InscripcionPostgrado', model_name='asignatura')
	column_list = ["Codigo", "U.C","Denominacion","Programa","Visto","Operaciones"]
	table = model.objects.filter(Cod_coordinacion = CodCoordinacion)
	temp = apps.get_model(app_label='InscripcionPostgrado', model_name='coordinacion')
	nameofcoordinacion = temp.objects.get(Cod_coordinacion = CodCoordinacion).Nombre_coordinacion
	form = AsignaturaForm(initial={'Cod_coordinacion': CodCoordinacion})
	form.fields['Cod_coordinacion'].widget = forms.HiddenInput()
	form.Cod_coordinacion = CodCoordinacion
	context = __contextTemplate__("asignaturas de " + nameofcoordinacion,column_list,table,False,form)
	return context

def __buildContextOferta__(request):
	model = apps.get_model(app_label='InscripcionPostgrado', model_name='se_ofrece')
	column_list = ["Código", "U.C","Denominación","Profesor","Programa","Horario"]
	cod = request.path.split("ofertas_")[1].split("/")[0]
	if "ofertas_" in request.path:
		table=model.objects.filter(Periodo = cod)
	else:
		table=model.objects.all()
	form = __returnForm__("",request)
	element = apps.get_model(app_label='InscripcionPostgrado', model_name='trimestre').objects.get(id=cod)
	context = __contextTemplate__(element.returnTrimWithAnio(),column_list,table,False,form)
	return context

# Funcion que dado los parametros listados rellena la plantilla
# de contexto que se va a pasar al front.
def __contextTemplate__(tableName, columnList,table,show_all_tables,givenForm):
	context = {
			'table_name' : tableName,
			'table_column_list' : columnList,
			'table' : table,
			'show_all_tables' : show_all_tables,
			'form' : givenForm
		}
	return context

# Funcion que construye una lista de parametros a partir
# de lo devuelto en el POST.
def __getParameters__(name,request):
	context=__getContext__(request,name,True)
	parameters = { }
	#Consigue los parametros uno por uno a partir del POST
	for i in context["table_column_list"]:
		parameters[i]=request.POST.get(i)
	#Si se esta en una coordinacion, el POST no devuelve el
	#codigo de la misma. Hay que colocarlo
	if "coordinacion_" in request.path:
		parameters["Cod_coordinacion"] = name
	return parameters

# Funcion que dependiendo de la tabla que se esta viendo
# crea los formularios respectivos para modificarla.
def __modififyDB__(name, parameters,request):
	form = __returnForm__(name,request)
	if form != None :
		if form.is_valid():
			form.save()
		else:
			raise
	else:
		if parameters == None:
			raise
		table = apps.get_model(app_label='InscripcionPostgrado', model_name=name)
		element=table.__createElement__(parameters)
		element.save()

# Funcion que dependiendo de la tabla retorna el fomulario
# correspondiente, o None si no es de los casos dados.
def __returnForm__(name,request):
	if "coordinacion" in name:
		if not request.POST:
			return CoordinacionForm()
		return CoordinacionForm(request.POST)
	elif "asignatura" in name:
		if not request.POST:
			return AsignaturaForm()
		return AsignaturaForm(request.POST)
	elif "profesor" in name:
		if not request.POST:
			return ProfesorForm()
		return ProfesorForm(request.POST)
	elif "pertenece" in name:
		if not request.POST:
			return PerteneceForm()
		return PerteneceForm(request.POST)
	elif "coordinacion_" in request.path:
		if not request.POST:
			form = AsignaturaForm(initial={'Cod_coordinacion': name})
			form.fields['Cod_coordinacion'].widget = forms.HiddenInput()
			return form
		form = AsignaturaForm(request.POST)
		return form
	elif "se_ofrece" in request.path:
		if not request.POST:
			return Se_OfreceForm()
		return Se_OfreceForm(request.POST)
	elif "ofertas" in request.path:
		if not request.POST:
			cod = request.path.split("ofertas_")[1].split("/")[0]
			form = Se_OfreceForm(initial={'Periodo': cod})
		else:
			form = Se_OfreceForm(request.POST)
		form.fields['Periodo'].widget = forms.HiddenInput()
		return form
	elif "trimestre" in request.path or "trimestre" in name.lower():
		if not request.POST:
			return TrimestreForm()
		return TrimestreForm(request.POST)	
	else:
		return None
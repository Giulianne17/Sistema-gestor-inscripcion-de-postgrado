from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
	context = {'table_name' : "Estudiante",
		'table_column_list' : Estudiante.__getallfieldNames__(),
		'table' : Estudiante.objects.all()
	}
	return render(request, 'crud/index.html', context)
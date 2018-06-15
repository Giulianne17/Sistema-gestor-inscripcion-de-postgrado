from InscripcionPostgrado.forms import *

def dataTemplate(Codasig,NombreAsig,CodCoord,Cred,Prog):
    form_data = {
            'Cod_asignatura': Codasig,
            'Nombre_asig': NombreAsig,
            'Cod_coordinacion': CodCoord,
            'Creditos': Cred,
            'Programa': Prog
        }
    return form_data

def addtoDB():
    addtoDBCoordAsig()
    addtoDBprof()
    addtoDBoferta()

def addtoDBCoordAsig():
    f = open('BDdatatxt/coordinaciones.txt','r')
    for line in f:
        temp = line.split(',')
        Cod,Nombre=temp[0],temp[1]
        dataG = {
            'Cod_coordinacion': Cod,
            'Nombre_coordinacion': Nombre,
        }
        Form = CoordinacionForm(data=dataG)
        if Form.is_valid():
            Form.save()
        else:
            print("form no valido")
            print(Form.errors)
    f.close()
    f = open('BDdatatxt/materias.txt','r')
    Programa = "http://gecousb.com.ve/guias/GECO/Programas%20Acad%C3%A9micos%20Ing.Computaci%C3%B3n/3er%20A%C3%B1o/Ingenier%C3%ADa%20de%20Software%20(CI-3715).pdf"
    for line in f:
        temp = line.split(',')
        Cod,Nombre,Cred=temp[0],temp[1],temp[2].split("\n")[0]
        CodCoord = Cod[0:2]
        dataG = dataTemplate(Cod,Nombre,CodCoord,Cred,Programa)
        Form = AsignaturaForm(data=dataG)
        if Form.is_valid():
            Form.save()
        else:
            print("form no valido")
            print(Form.errors)
    f.close()

def addtoDBprof():
    f = open('BDdatatxt/prof.txt','r')
    for line in f:
        [CI,Apellidos,Nombres,CodCoord] = line.split(',')
        CodCoord=CodCoord.split("\n")[0]
        dataG = {
            'Id_prof': CI,
            'Apellidos': Apellidos,
            'Nombres': Nombres,
            'Cod_coordinacion': CodCoord
        }
        Form = ProfesorForm(data=dataG)
        if Form.is_valid():
            Form.save()
        else:
            print("form no valido")
            print(Form.errors)
    f.close()

def addtoDBoferta():
    f = open('BDdatatxt/oferta.txt','r')
    for line in f:
        [Id_prof,Cod_asignatura,Horario,Dia,Periodo,Anio,CodCoord] = line.split(',')
        CodCoord=CodCoord.split("\n")[0]
        dataG = {
            'Id_prof': Id_prof,
            'Cod_asignatura': Cod_asignatura,
            'Horario': Horario,
            'Dia': Dia,
            'Periodo': Periodo,
            'Anio': Anio,
            'Cod_coordinacion': CodCoord
        }
        Form = Se_OfreceForm(data=dataG)
        if Form.is_valid():
            Form.save()
        else:
            print("form no valido")
            print(Form.errors)
    f.close()

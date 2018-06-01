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
    f = open('coordinaciones.txt','r')
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
    f = open('materias.txt','r')
    Programa = "https://pythex.org/"
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
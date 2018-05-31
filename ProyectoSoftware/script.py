from InscripcionPostgrado.models import *

def dataTemplate(Codasig,NombreAsig,CodCoord,Cred,Prog):
    form_data = {
            'Cod_asignatura': Codasig,
            'Nombre_asig': NombreAsig,
            'Cod_coordinacion': CodCoord,
            'Creditos': Cred,
            'Programa': Prog
        }


CI-7541 TEORIA DE LA COMPUTACIÓN    4
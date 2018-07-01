def writeFilePath(requestmethod,path,functionName):
    ''' Función que dado un método, path y nombre de la función/vista
    imprime en un archivo el flujo básico correspondiente
    
    NOTA: Por el momento, una vez conseguido el flujo básico
    correspondiente a la entrega de la fase, esta función deja de ser
    utilizada.
    Para utilizarla, importe en views.py y coloque bajo la firma de la
    función un llamado a writeFilePath con los atributos correspondientes.
    '''
    with open('prueba','r') as g:
        listoflines = g.readlines()
        if len(listoflines)>0:
            OldPath = listoflines[len(listoflines)-1]
        else:
            OldPath="None"
    if OldPath!="None" and "FLUJO BÁSICO" not in OldPath:
        with open('prueba','a') as f:
            if "favicon" not in path:
                lastMethod = OldPath.split(" al path ")[0].split("Método ")[1]
                OldPath = OldPath.split("\" usando las funciones")[0].split("al path \"")[1]
                if path not in OldPath or path!=OldPath or requestmethod!=lastMethod:
                    string = "\nMétodo "+requestmethod+" al path \""+path+"\" usando las funciones "+functionName
                    if not FindSameLine(string):
                        f.write(string)
                else:
                    f.write(">>"+functionName)
    else:
        with open('prueba','a') as f:
            if "favicon" not in path:
                f.write("\nMétodo "+requestmethod+" al path \""+path+"\" usando las funciones "+functionName)


def FindSameLine(linetofind):
    ''' Función auxiliar que busca en el archivo de flujo básico si la
    línea a agregar tiene parámetros que ya han sido agregados con
    anterioridad.
    '''
    linetofind = linetofind.strip("\n")
    method = linetofind.split(" al path ")[0].split("Método ")[1]
    path = linetofind.split("\" usando las funciones")[0].split("al path \"")[1]
    with open('prueba','r') as file:
        for line in file:
            if "FLUJO BÁSICO" not in line:
                currentmethod = line.split(" al path ")[0].split("Método ")[1]
                currentpath = line.split("\" usando las funciones")[0].split("al path \"")[1]
                if linetofind in line or (method in currentmethod and path==currentpath):
                    return True
        return False
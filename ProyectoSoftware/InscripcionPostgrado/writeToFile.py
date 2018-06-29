def writeFilePath(path,functionName):
    with open('prueba','a') as f:
        with open('prueba','r') as g:
            listoflines = g.readlines()
            if len(listoflines)!=0:
                OldPath = listoflines[len(listoflines)-1]
            else:
                OldPath="None"
        if "favicon" not in path:
            if path not in OldPath:
                f.write("\nEstamos en "+path+" llegando desde "+functionName)
            else:
                f.write(">>"+functionName)
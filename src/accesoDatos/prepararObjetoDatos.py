#To succesfuslly invoke the function, as it is in another folder,
#we need to specify its path with 'sys'. And then it is possible to call it.
from sys import path as systemPath
systemPath.insert(0, './src/accesoDatos/')
from prepararXML import prepararXML
from prepararTXT import prepararTXT

def prepararObjetoDatos(*args):
    # (ruta acceso, parametros configuración)
    # Open Closed Principle
    # Con un diccionario simulamos el comportamiento
    # de un switch-case.
    # La extensión del archivo sirve como clave del diccionario.
    # El valor es un string con el nombre de la funcion a invocar.
    # No conseguimos un OCP estricto porque es necesario modificar
    # el diccionario (aunque solo sea extendiendolo) para incluir
    # nuevos tipos de ficheros.

    posicionExtension = args[0].index('.')
    extensionFichero = args[0][posicionExtension + 1:]
    # Hay que impedir que la funcion se ejecute al construir el diccionario
    operaciones = {"xml": "prepararXML" + str(tuple(args)),
                   "xspf": "prepararXML" + str(tuple(args)),
                   "txt": "prepararTXT" + str(tuple(args))
                   }

    # Devolvemos la funcion adecuada:
    # prepararXML(data, xmlns)
    # prepararTXT(data, argumento)
    # eval provoca que se ejecute la funcion
    return eval(operaciones[extensionFichero])

if __name__ == "__main__":
    
    #To succesfuslly invoke the function, as it is in another folder,
    #we need to specify its path with 'sys'. And then it is possible to call it.
    from sys import path as systemPath
    systemPath.insert(0, './src/')
    from vlcVariables import data, xmlns

    #Prueba con fichero con extension XML.
    libreria = prepararObjetoDatos(data, xmlns)

    print('\n' + '#' * 3 + " LIBRERIA " + '#' * 3 + '\n')
    print(libreria)

    #Prueba con fichero con extension TXT.
    '''data = "mockfile.txt"

    libreria = prepararObjetoDatos(data, "otro")

    print('\n' + '#' * 3 + " LIBRERIA " + '#' * 3 + '\n')
    print(libreria)'''
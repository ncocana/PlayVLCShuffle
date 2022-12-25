
# un intento de implementar el patron SOLID OCP (Open Closesd)
# dentro del patron fachada para acceder
# a distintos ficheros

import xml.etree.ElementTree as ET


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


def prepararXML(data, xmlns):

    arbol = ET.parse(data)
    root = arbol.getroot()

    trackList = root.find("xmlns:trackList", xmlns)

    libreria = {track.find("xmlns:title", xmlns).text:
                {
                    "artist": track.find("xmlns:creator", xmlns).text,
                    "album": track.find("xmlns:album", xmlns).text,
                    "location": track.find("xmlns:location", xmlns).text
                }
                for track in trackList}

    return libreria


def prepararTXT(data, opciones):
    # mock function
    return "Es un fichero de texto"


if __name__ == "__main__":
    
    from vlcVariables import data, xmlns

    libreria = prepararObjetoDatos(data, xmlns)

    print('\n' + '#' * 3 + " LIBRERIA " + '#' * 3 + '\n')
    print(libreria)

    data = "mockfile.txt"

    libreria = prepararObjetoDatos(data, "otro")

    print('\n' + '#' * 3 + " LIBRERIA " + '#' * 3 + '\n')
    print(libreria)

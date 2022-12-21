# Existe una version comentada de este codigo

import random

from accesoDatosOCP import prepararObjetoDatos


## UTILIDADES DE DEPURACION ##

# No utilizo casos test:
# Empleo precondiciones y postcondiciones para chequear el estado
# de las estructuras de datos que modifico

def checkSeleccionaCancionRandom(cancion, libreria):

    # precondiciones
    assert isinstance(cancion, str)
    assert isinstance(libreria, dict)

    if cancion not in libreria:
        return False
    else:
        return True


def checkPlaySuffle(playList):

    assert isinstance(playList, dict)

    listaCanciones = list(playList.values())

    for item in listaCanciones:
        if listaCanciones.count(item) > 1:
            return False
    return True


## RUTINAS DE UTILIDADES ##


def check_modules():

    try:
        import sys
    except(ImportError):
        raise SystemExit #exit()

    dependencies = ['shlex', 'os', 'subprocess', 'random', 
                    # 'touche turtle' # disparar bloque try
                    ]

    try:
        for dependency in dependencies:
            if dependency not in (sys.stdlib_module_names):
                raise ModuleNotFoundError(str(dependency)) # Builtin exception
    except ModuleNotFoundError as e:
        # sys,exit() cleanup actions specified by finally clauses of try statements are honored
        e_type, e_name, e_trace = sys.exc_info()
        sys.exit("Modulo %s no encontrado" % (str(e_name)))
    except AttributeError as e:
        # python exception message capturing
        sys.exit(str(e))
    else:
        # scope de variables locales en el try /except
        print("Dependencias %s presentes en el sistema" % (', '.join(dependencies)))
    finally:
        print("Dependencias de modulos chequeadas")


def seleccionaCancionRandom(libreria):

    assert isinstance(libreria, dict)

    tituloCancion = random.choice(list(libreria.keys()))

    assert checkSeleccionaCancionRandom(
        tituloCancion, libreria), "la cancion no es una clave del diccionario de canciones"

    return str(tituloCancion)


def iniciarPlayList(numeroCancion):

    claveDiccionarioPlayList = numeroCancion

    def appendCancion(cancion, playList):

        assert isinstance(playList, dict), "playList no es un diccionario"
        assert cancion not in list(playList.values())

        nonlocal claveDiccionarioPlayList
        claveDiccionarioPlayList += 1
        playList[claveDiccionarioPlayList] = str(cancion)
        return claveDiccionarioPlayList

    return appendCancion


## FUNCIONES PRINCIPALES ##


def imprimirCancionesReproducidas(playList):

    assert isinstance(playList, dict)

    for numeroCancion in sorted(playList.keys()):
        print(str(numeroCancion) + ": " + str(playList[numeroCancion]))


def lanzarVLC(libreria, playList):

    # Las canciones han de estar en un directorio llamado biblioteca
    # en el directorio de la aplicacion.
    # Han de ser expresamente las incluidas en el diccionario libreria.

    import subprocess
    import shlex
    import os

    linuxPathVLC = "C:/Program Files/VideoLAN/VLC/vlc.exe"
    lineaComandoVLC = linuxPathVLC
    separador = " "

    for numeroCancion in sorted(playList.keys()):
        tituloCancion = playList[numeroCancion]
        try:
            rutaAccesoFichero = libreria[tituloCancion]["location"]
        except KeyError:
            print("la cancion " + str(tituloCancion) +
                  " no se encuentra en la biblioteca")
        else:
            if rutaAccesoFichero.find("file://") == 0:
                rutaAccesoFichero = rutaAccesoFichero[7:]
            else:
                pass

            if os.path.exists(str(rutaAccesoFichero)):
                lineaComandoVLC = lineaComandoVLC + \
                    separador + str(rutaAccesoFichero)
            else:
                pass

    # Popen necesita una lista de string
    args = shlex.split(lineaComandoVLC)

    try:
        procesoVLC = subprocess.Popen(args)
        # procesoVLC = subprocess.Popen(["/usr/bin/vlc", "./biblioteca/California_Uber_Alles.mp3", "./biblioteca/Seattle_Party.flac"])
    except OSError:
        print("el fichero no existe")
    except ValueError:
        print("argumentos invalidos")
    else:
        print("lanzando VLC con lista aleatoria")


def playShuffle(libreria, playList):

    # precondicion
    assert isinstance(libreria, dict), "libreria no es un diccionario"

    numeroCancion = 0
    actualizarPlayList = iniciarPlayList(numeroCancion)

    continuar = True

    while continuar:

        cancion = seleccionaCancionRandom(libreria)

        if cancion not in list(playList.values()):
            numeroCancionActual = actualizarPlayList(cancion, playList)
            print("Seleccionada: " + str(playList[numeroCancionActual]))
        else:
            pass

        if len(libreria) == len(playList):
            continuar = False
            print("Se han incluido todas las canciones de la biblioteca")

    # postcondicion
    assert checkPlaySuffle(playList), "cancion repetida"

    return True


## PROGRAMA PRINCIPAL ##


def playShuffleVLC(libreria, playList):

    check_modules()

    playShuffle(libreria, playList)

    imprimirCancionesReproducidas(playList)

    lanzarVLC(libreria, playList)


if __name__ == '__main__':

    # espacios de nombres de los elementos
    # del schema xspf (por defecto) y vlc
    xmlns = {"xmlns": "http://xspf.org/ns/0/",
             "xmlns:vlc": "http://www.videolan.org/vlc/playlist/ns/0/"}

    # origen de los datos: un fichero XML
    data = "listaPlayShuffleVLC.xspf"

    '''
    Estructuras de datos en memoria:

    playList ={ 1: "titulo cancion", 2: "titulo cancion" ... }
    libreria = {"California_Uber_Alles.mp3":
                    {"track-number": 3,
                     "artist": "Dead Kennedys",
                     "album": "Dead Kennedys",
                     "location": "./biblioteca/California_Uber_Alles.mp3"},
                "Seattle_Party":
                    {"track-number": 1,
                     "artist": "Chastity Belt",
                     "album": "No regrets",
                     "location": "./biblioteca/Seattle_Party.flac"},
                "King_Kunta":
                    {"track-number": 3,
                     "artist": "Kendrick Lamar",
                     "album": "To Pimp A Butterfly",
                     "location": "./biblioteca/King_Kunta.mp3"}
                }
    '''

    playList = {}

    libreria = prepararObjetoDatos(data, xmlns)

    playShuffleVLC(libreria, playList)

def lanzarVLC(libreria, playList):

    # Las canciones han de estar en un directorio llamado biblioteca
    # en el directorio de la aplicacion.
    # Han de ser expresamente las incluidas en el diccionario libreria.

    import subprocess
    import shlex
    import os

    windowsPathVLC = "C:/Program Files/VideoLAN/VLC/vlc.exe"
    lineaComandoVLC = windowsPathVLC
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
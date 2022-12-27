#To succesfuslly invoke the function, as it is in another folder,
#we need to specify its path with 'sys'. And then it is possible to call it.
from sys import path as systemPath
systemPath.insert(0, './src/')
from shufflePlayList.iniciarPlayList import iniciarPlayList
from shufflePlayList.seleccionaCancionRandom import seleccionaCancionRandom
from checkRoutines.checkPlaySuffle import checkPlaySuffle

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
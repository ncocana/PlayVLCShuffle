from iniciarPlayList import iniciarPlayList
from seleccionaCancionRandom import seleccionaCancionRandom
from checkPlaySuffle import checkPlaySuffle

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
#To succesfuslly invoke the function, as it is in another folder,
#we need to specify its path with 'sys'. And then it is possible to call it.
from sys import path as systemPath
systemPath.insert(0, './src/')
from checkRoutines.checkSeleccionaCancionRandom import checkSeleccionaCancionRandom
import random

def seleccionaCancionRandom(libreria):

    assert isinstance(libreria, dict)

    tituloCancion = random.choice(list(libreria.keys()))

    assert checkSeleccionaCancionRandom(
        tituloCancion, libreria), "la cancion no es una clave del diccionario de canciones"

    return str(tituloCancion)
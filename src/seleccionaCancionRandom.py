import random
from checkSeleccionaCancionRandom import checkSeleccionaCancionRandom

def seleccionaCancionRandom(libreria):

    assert isinstance(libreria, dict)

    tituloCancion = random.choice(list(libreria.keys()))

    assert checkSeleccionaCancionRandom(
        tituloCancion, libreria), "la cancion no es una clave del diccionario de canciones"

    return str(tituloCancion)
from accesoDatosOCP import prepararObjetoDatos
from check_modules import check_modules
from playShuffle import playShuffle
from imprimirCancionesReproducidas import imprimirCancionesReproducidas
from lanzarVLC import lanzarVLC
from vlcVariables import playList, libreria

def playShuffleVLC(libreria, playList):

    check_modules()

    playShuffle(libreria, playList)

    imprimirCancionesReproducidas(playList)

    lanzarVLC(libreria, playList)

if __name__ == '__main__':

    playShuffleVLC(libreria, playList)
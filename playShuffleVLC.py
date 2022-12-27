from src.checkRoutines.check_modules import check_modules
from src.shufflePlayList.playShuffle import playShuffle
from src.imprimirCancionesReproducidas import imprimirCancionesReproducidas
from src.lanzarVLC import lanzarVLC
from src.datos.vlcVariables import playList, libreria

def playShuffleVLC(libreria, playList):

    check_modules()

    playShuffle(libreria, playList)

    imprimirCancionesReproducidas(playList)

    lanzarVLC(libreria, playList)

if __name__ == '__main__':

    playShuffleVLC(libreria, playList)
def imprimirCancionesReproducidas(playList):

    assert isinstance(playList, dict)

    for numeroCancion in sorted(playList.keys()):
        print(str(numeroCancion) + ": " + str(playList[numeroCancion]))
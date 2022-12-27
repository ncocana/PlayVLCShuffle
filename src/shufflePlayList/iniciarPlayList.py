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
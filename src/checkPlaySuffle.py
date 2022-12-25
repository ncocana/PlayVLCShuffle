def checkPlaySuffle(playList):

    assert isinstance(playList, dict)

    listaCanciones = list(playList.values())

    for item in listaCanciones:
        if listaCanciones.count(item) > 1:
            return False
    return True
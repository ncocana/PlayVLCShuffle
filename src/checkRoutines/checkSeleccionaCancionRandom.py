def checkSeleccionaCancionRandom(cancion, libreria):

    # precondiciones
    assert isinstance(cancion, str)
    assert isinstance(libreria, dict)

    if cancion not in libreria:
        return False
    else:
        return True

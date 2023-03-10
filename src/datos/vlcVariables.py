#To succesfuslly invoke the function, as it is in another folder,
#we need to specify its path with 'sys'. And then it is possible to call it.
from sys import path as systemPath
systemPath.insert(0, './src/')
from accesoDatos.prepararObjetoDatos import prepararObjetoDatos
from pathlib import Path
from os import getcwd as getCurrentDirectory

# espacios de nombres de los elementos
# del schema xspf (por defecto) y vlc
xmlns = {"xmlns": "http://xspf.org/ns/0/",
        "xmlns:vlc": "http://www.videolan.org/vlc/playlist/ns/0/"}

# origen de los datos: un fichero XML
working_directory = Path(getCurrentDirectory())
pathFileXML = working_directory / "src" / "datos" / "listaPlayShuffleVLC.xspf"
data = str(pathFileXML)

playList = {}

libreria = prepararObjetoDatos(data, xmlns)

'''
Estructuras de datos en memoria:

playList ={ 1: "titulo cancion", 2: "titulo cancion" ... }
libreria = {"California_Uber_Alles.mp3":
                {"track-number": 3,
                 "artist": "Dead Kennedys",
                 "album": "Dead Kennedys",
                 "location": "./biblioteca/California_Uber_Alles.mp3"},
             "Seattle_Party":
                {"track-number": 1,
                 "artist": "Chastity Belt",
                 "album": "No regrets",
                 "location": "./biblioteca/Seattle_Party.flac"},
             "King_Kunta":
                {"track-number": 3,
                 "artist": "Kendrick Lamar",
                 "album": "To Pimp A Butterfly",
                 "location": "./biblioteca/King_Kunta.mp3"},
             "Against_the_moon":
                {"track-number": 4,
                 "artist": "Unknown",
                 "album": "Unknown",
                 "location": "./biblioteca/against_the_moon.mp3"},
             "Elvis_Flaming_Star":
                {"track-number": 5,
                 "artist": "Unknown",
                 "album": "Unknown",
                 "location": "./biblioteca/Elvis_Flaming_Star.mp3"},
             "Headless":
                {"track-number": 6,
                 "artist": "Unknown",
                 "album": "Unknown",
                 "location": "./biblioteca/Headless.mp3"}
            }
'''
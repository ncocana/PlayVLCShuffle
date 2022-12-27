import xml.etree.ElementTree as ET

def prepararXML(data, xmlns):

    arbol = ET.parse(data)
    root = arbol.getroot()

    trackList = root.find("xmlns:trackList", xmlns)

    libreria = {track.find("xmlns:title", xmlns).text:
                {
                    "artist": track.find("xmlns:creator", xmlns).text,
                    "album": track.find("xmlns:album", xmlns).text,
                    "location": track.find("xmlns:location", xmlns).text
                }
                for track in trackList}

    return libreria
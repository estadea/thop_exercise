# Data una lista di tragitti
# x = [(p1, a1), (p2, a2), …]
# dove ogni tupla (pi, ai) indica il tragitto da pi ad ai
# Scrivi una funzione (preferibilmente in python) che ricostruisce il percorso completo.
#
# Esempio
#
#  x = [(roma, napoli), (milano, torino), (napoli, genova), (genova , milano)]
# y  = unisci_tragitti(x)
# # print(y) = [roma, napoli, genova, milano, torino]
#
# Spiegazione:
#
# Roma non compare mai come destinazione e deve essere quindi il punto di partenza.
# Da roma si va a napoli, da napoli si va a genova, da genova a milano e da milano a torino.


def PathBuilder(cities):
    # index data in hashtables
    cityHash = {}
    destinations = set()
    for (a,b) in cities:
      cityHash[a] = b
      destinations.add(b)

    # find the city that is never a destination and set is as starting point
    startFound = 0
    startingPoint = ""
    for (a,_) in cities:
      if a not in destinations:
        if startFound == 1:
            print("multiple starting points")
            exit()
        startingPoint = a
        startFound = 1;


    # transverse the path using the hashtable
    path = [startingPoint]
    while startingPoint in cityHash:
        startingPoint = cityHash[startingPoint]
        path.append(startingPoint)

    return path

cities = [ ('Springfield','Charming') , ('Charming','WildWildWest'),  ('Roma','Tortuga') ,('Tortuga','SouthPark'),('SouthPark','Springfield')]

print(PathBuilder(cities))

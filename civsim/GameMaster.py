from civsim.CIty.City import City


class GameMaster:
    def __init__(self):
        self.cities = []
        self.cityNumber = 0

    def addCity(self, num):
        city = City(num)
        self.cities.append(city)
        self.cityNumber += 1
import json
from Civsim.City.City import City
from Civsim.City.House import House
from Civsim.City.Workplace.EResources import EResources
from Civsim.City.Workplace.Workplace import Workplace
from Civsim.Human.Human import Human
from Civsim.Mayor.Mayor import Mayor


class Loader:
    def __init__(self, gm):
        self.gm = gm

    def loadCity(self, savefile):
        data = json.load(savefile)
        savedCity = data
        loadedCity = City(-1, 0, self.gm)
        loadedCity.mayor = Mayor(loadedCity)
        loadedCity.name = savedCity["name"]
        loadedCity.year = savedCity["year"]
        self.gm.cities.append(loadedCity)
        self.gm.mayors.append(loadedCity.mayor)
        for i in savedCity["storage"].keys():
            if i == "FOOD":
                loadedCity.storage[EResources.FOOD] = savedCity["storage"][i]
            if i == "BRICKS":
                loadedCity.storage[EResources.BRICKS] = savedCity["storage"][i]
        loadedCity.workplaces += self.loadWorkplaces(savedCity["workplaces"], loadedCity)
        loadedCity.houses += self.loadHouses(savedCity["houses"])
        self.loadHumans(savedCity["population"], loadedCity)

    def loadWorkplaces(self, workplaces, city):
        out = []
        for workplace in workplaces:
            res = None
            if workplace["resource"] == 1:
                res = EResources.FOOD
            if workplace["resource"] == 2:
                res = EResources.BRICKS
            loadedWorkplace = Workplace(res, city)
            loadedWorkplace.id = workplace["id"]
            out.append(loadedWorkplace)
        return out

    def loadHouses(self, houses):
        out = []
        for house in houses:
            loadedHouse = House()
            loadedHouse.id = house["id"]
            out.append(loadedHouse)
        return out

    def loadHumans(self, humans, city):
        for human in humans:
            loadedHuman = Human()
            loadedHuman.id = human["id"]
            loadedHuman.age = human["age"]
            loadedHuman.hunger = human["hunger"]
            loadedHuman.happiness = human["happiness"]
            loadedHuman.birthDate = human["birthDate"]
            loadedHuman.city = city
            loadedHuman.isAdult()

            for workplace in city.workplaces:
                if human["workplace"] is None:
                    break
                if human["workplace"] == workplace.id:
                    workplace.workforce.append(loadedHuman)
                    loadedHuman.workplace = workplace
            for house in city.houses:
                if human["house"] is None:
                    break
                if human["house"] == house.id:
                    house.residents.append(loadedHuman)
                    loadedHuman.house = house

            city.population.append(loadedHuman)

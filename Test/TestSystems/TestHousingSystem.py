import unittest

from Civsim.City.City import City
from Civsim.City.House import House
from Civsim.Human.Human import Human


class TestHousingSystem(unittest.TestCase):
    def testAccommodateHuman(self):
        city = City(0, 0, 0)
        human = Human(20, city)
        city.population.append(human)
        house = House()

        city.houses.append(house)
        city.housingSystem.accommodatePeople()

        self.assertTrue(human.house is not None)

    def testAccommodateMorePeople(self):
        city = City(0, 0, 0)

        human1 = Human(20, city)
        city.population.append(human1)
        human2 = Human(20, city)
        city.population.append(human2)
        house = House()

        city.houses.append(house)
        city.housingSystem.accommodatePeople()

        for human in city.population:
            self.assertTrue(human.house is not None)

    def testNotAvailableHouse(self):
        city = City(0, 0, 0)
        house = House()
        city.houses.append(house)

        for i in range(4):
            human = Human(20, city)
            human.house = house
            house.residents.append(human)
            city.population.append(human)

        homeless = Human(20, city)

        city.housingSystem.accommodatePeople()

        self.assertTrue(homeless.house is None)

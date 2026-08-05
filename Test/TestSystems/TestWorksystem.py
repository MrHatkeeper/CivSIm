import unittest

from Civsim.City.City import City
from Civsim.City.Workplace.EResources import EResources
from Civsim.City.Workplace.Workplace import Workplace
from Civsim.Human.Human import Human


class TestWorkSystem(unittest.TestCase):
    def testAssignWorker(self):
        city = City(0, 0, 0)
        human = Human(20, city, 0)
        human.adult = True
        city.population.append(human)

        workplace = Workplace(EResources.FOOD, city)
        city.workplaces.append(workplace)
        city.workplaceSystem.assignWorkplace()

        self.assertTrue(human.workplace is not None)

    def testProducedResource(self):
        city = City(0, 0, 0)
        human = Human(20, city, 0)
        human.adult = True
        city.population.append(human)

        workplace = Workplace(EResources.FOOD, city)
        city.workplaces.append(workplace)
        city.workplaceSystem.assignWorkplace()
        city.workplaceSystem.updateResources()

        self.assertEqual(city.storage[EResources.FOOD], 5)

    def testNoFreeWorkingPosition(self):
        city = City(0, 0, 0)
        city.workplaces = []
        workplace = Workplace(EResources.FOOD, city)
        city.workplaces.append(workplace)

        for i in range(4):
            human = Human(20, city, 0)
            city.population.append(human)
            workplace.workforce.append(human)

        workless = Human(20, city, 0)
        city.population.append(workless)
        city.workplaceSystem.assignWorkplace()

        self.assertEqual(workless.workplace, None)

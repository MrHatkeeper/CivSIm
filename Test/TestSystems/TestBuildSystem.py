import unittest

from Civsim.City.City import City
from Civsim.City.Workplace.EResources import EResources


class TestBuildSystem(unittest.TestCase):
    def testBuildHouse(self):
        city = City(0, 3, 0)
        city.storage[EResources.BRICKS] = 99999999
        if city.buildSystem.canBuild("house"):
            city.buildSystem.buildHouse()

        self.assertEqual(city.storage[EResources.BRICKS], 99999989)
        self.assertEqual(len(city.houses), 2)

    def testNotEnoughMaterial(self):
        city = City(0, 3, 0)
        city.storage[EResources.BRICKS] = 0
        self.assertFalse(city.buildSystem.canBuild("house"))

    def testCanBuildFarm(self):
        city = City(0, 3, 0)
        city.storage[EResources.BRICKS] = 99999999

        if city.buildSystem.canBuild("farmHouse"):
            city.buildSystem.buildWorkplace(EResources.FOOD)
        self.assertEqual(city.storage[EResources.BRICKS], 99999959)

        self.assertEqual(len(city.workplaces), 3)

    def testCanBuildBrickHouse(self):
        city = City(0, 3, 0)
        city.storage[EResources.BRICKS] = 99999999

        if city.buildSystem.canBuild("brickHouse"):
            city.buildSystem.buildWorkplace(EResources.FOOD)
        self.assertEqual(city.storage[EResources.BRICKS], 99999959)
        self.assertEqual(len(city.workplaces), 3)

import unittest

from Test.TestHuman import TestHuman
from Test.TestSystems.TestBuildSystem import TestBuildSystem
from Test.TestSystems.TestHousingSystem import TestHousingSystem
from Test.TestSystems.TestPopulationSystem import TestPopulationSystem
from Test.TestSystems.TestWorksystem import TestWorkSystem


def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(TestHousingSystem))
    suite.addTests(loader.loadTestsFromTestCase(TestPopulationSystem))
    suite.addTests(loader.loadTestsFromTestCase(TestWorkSystem))
    suite.addTests(loader.loadTestsFromTestCase(TestBuildSystem))
    suite.addTests(loader.loadTestsFromTestCase(TestHuman))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from Civsim.City.City import City

from Civsim.Misc import PopInfo, Metrics


class HistorySystem:
    def __init__(self, city: City):
        self.city = city
        self.populationData = []
        self.populationData = {"year": [0], "total": [0], "homeless": [0]}
        self.happinessData = {"year": [0], "averageHappiness": [0],
                              "meanHappiness": [0]}

    def saveData(self):
        self.populationData["year"].append(self.city.year)
        self.populationData["total"].append(len(self.city.population))
        self.populationData["homeless"].append(PopInfo.numOfHomeless(self.city))

        self.happinessData["year"].append(self.city.year)
        self.happinessData["averageHappiness"].append(Metrics.getAverage("happiness", self.city))
        self.happinessData["meanHappiness"].append(Metrics.getMeanHappiness(self.city))

    def showData(self):
        populationData = pd.DataFrame(self.populationData)
        happinessData = pd.DataFrame(self.happinessData)
        return [populationData, happinessData]

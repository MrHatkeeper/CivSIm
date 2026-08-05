import json
from datetime import datetime

from Civsim.City.City import City


def exportCity(city: City):
    """
    Metoda pro uložení stavu města.
    :param city: které město se má uložit
    """
    save = {
        "name": city.name,
        "year": city.year,
        "population": [],
        "workplaces": [],
        "houses": [],
        "storage": {},
        "populationData": {"year": [], "total": [], "homeless": []},
        "happinessData": {"year": [], "averageHappiness": [], "meanHappiness": []},
    }
    for storage in city.storage:
        save["storage"][storage.name] = city.storage[storage]

    for human in city.population:
        humanSave = {"id": str(human.id), "age": human.age, "happiness": human.happiness, "hunger": human.hunger,
                     "house": None, "workplace": None, "birthDate": human.birthDate}
        if human.house is not None:
            humanSave["house"] = str(human.house.id)
        if human.workplace is not None:
            humanSave["workplace"] = (str(human.workplace.id))

        save["population"].append(humanSave)

    for workplace in city.workplaces:
        workplaceSave = {"id": str(workplace.id), "workforce": [], "resource": workplace.resource.value}
        save["workplaces"].append(workplaceSave)

    for house in city.houses:
        houseSave = {"id": str(house.id)}
        save["houses"].append(houseSave)

    for populationData in city.historySystem.populationData.keys():
        for record in city.historySystem.populationData[populationData]:
            save["populationData"][populationData].append(str(record))

    for happinessData in city.historySystem.happinessData.keys():
        for record in city.historySystem.happinessData[happinessData]:
            save["happinessData"][happinessData].append(str(record))

    fileName = datetime.now()
    with open(f"Saves/{fileName}.json", "w", encoding="utf-8") as f:
        json.dump(save, f, ensure_ascii=False, indent=4)

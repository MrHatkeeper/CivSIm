from datetime import datetime
import json

class Saver:
    def exportCity(self, city):
        save = {
            "name": city.name,
            "year": city.year,
            "population": [],
            "workplaces": [],
            "houses": [],
            "storage": {},
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
            houseSave = {"id": str(house.id), "residents": []}
            save["houses"].append(houseSave)

        saveJson = json.dumps(save)
        fileName = datetime.now()
        with open(f"Saves/{fileName}.json", "w", encoding="utf-8") as f:
            json.dump(saveJson, f, ensure_ascii=False, indent=4)

def accommodateHuman(human, house):
    human.house = house
    house.residents.append(human)

class HousingSystem:
    def __init__(self, city):
        self.city = city

    def accommodatePeople(self):
        emptyHouses = [h for h in self.city.houses if len(h.residents) < h.capacity]
        houseIndex = 0
        for human in self.city.population:
            if human.house is not None:
                continue
            if houseIndex >= len(emptyHouses):
                break
            house = emptyHouses[houseIndex]
            accommodateHuman(human, house)
            if len(house.residents) >= house.capacity:
                houseIndex += 1

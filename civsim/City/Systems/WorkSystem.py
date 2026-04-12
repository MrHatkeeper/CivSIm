class WorkSystem:
    def __init__(self, city):
        self.city = city

    def updateWork(self):
        self.assignWorkplace()
        self.updateResources()

    def assignWorkplace(self):
        from civsim.Misc import CityInfo
        unemployed = CityInfo.getUnemployed(self.city)
        for workplace in self.city.workplaces:
            if len(unemployed) == 0:
                break
            freeSlots = workplace.capacity - len(workplace.workforce)
            if freeSlots > 0:
                toAssign = unemployed[:freeSlots]
                for human in toAssign:
                    human.workplace = workplace
                    workplace.workforce.append(human)
                unemployed = unemployed[freeSlots:]

    def updateResources(self):
        for workplace in self.city.workplaces:
            workplace.produceResource()
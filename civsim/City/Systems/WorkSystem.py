from civsim.Misc import PopInfo


class WorkSystem:
    def __init__(self, city):
        self.city = city

    def updateWork(self):
        """
        Funkce slouží jako přístupový bod pro WorkSystem z přiřazeného City.
        """
        self.assignWorkplace()
        self.updateResources()

    def assignWorkplace(self):
        """
        Vezme všechny dospělé a nezaměstnané lidi a přiřadí jim pracovní místa.

        Upravuje human.workplace a workplace.workforce.
        """
        unemployed = PopInfo.getUnemployed(self.city)
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
        """
        Metoda projde všechny Workplace ve městě a přidá jejich produkci do skladu.
        """
        for workplace in self.city.workplaces:
            workplace.produceResource()
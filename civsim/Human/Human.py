class Human:
    def __init__(self, startAge: int = 0):
        self.name = self.generateName()
        self.age = startAge
        self.happiness = 100
        self.hunger = 0
        self.house = None
        self.isAdult = False

    #TODO:
    def generateName(self) -> str:
        return "A"
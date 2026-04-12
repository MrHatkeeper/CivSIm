from civsim.Config import Config


class House:
    def __init__(self):
        self.capacity = Config.HOUSE_MAX_RESIDENTS.value
        self.residents = []
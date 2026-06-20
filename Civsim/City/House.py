import uuid

from Civsim.Config import Config


class House:
    def __init__(self):
        self.id = uuid.uuid4()
        self.capacity = Config.HOUSE_MAX_RESIDENTS.value
        self.residents = []
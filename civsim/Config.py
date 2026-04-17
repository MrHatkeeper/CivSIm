from enum import Enum
class Config(Enum):
    """
    Soubor s fixními hodnotami.
    """

    """
    Human config
    """
    HUNGER_RATE = 2
    ADULT_AGE = 2
    BIRTH_RATIO = 50
    IS_HOUSED_INC = 2
    HUNGRY_INC = 2
    DEATH_BORDER = 30
    HOMELESS_BIRTH_RATIO = 0.3

    """
    Workplace config
    """
    PROD_RATIO = 5

    """
    Building config
    """
    HOUSE_COST = 10
    WORKPLACE_COST = 10
    WORKPLACE_MAX_RESIDENTS = 4
    HOUSE_MAX_RESIDENTS = 4

    """
    Mayor score config
    """
    HUMAN_SCORE = 10
    HOUSE_SCORE = 10
    FREE_HOUSING_SPACE_MULT = 1.5
    HOMELESS_MULT = 1.5
    AVG_HAPPINESS_MULT = 1.5
    AVG_HUNGER_MULT = 5
    MAYOR_LOOK_AHEAD = 3




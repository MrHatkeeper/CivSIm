import streamlit as st

from Civsim.City.Workplace.EResources import EResources
from Civsim.Misc import EconInfo


def renderHousing(city):
    st.subheader("Housing")

    data = {
        "Type": [
            "House",
            "Farm",
            "Brick house"
        ],
        "Number of places": [
            EconInfo.numOfHouses(city),
            EconInfo.numOfWorkplaces(city, EResources.FOOD),
            EconInfo.numOfWorkplaces(city, EResources.BRICKS)
        ],
        "Occupied spaces": [
            EconInfo.numOfOccupiedLivingSpaces(city),
            EconInfo.numOfOccupiedWorkPlaces(city, EResources.FOOD),
            EconInfo.numOfOccupiedWorkPlaces(city, EResources.BRICKS)
        ],

        "Free spaces": [
            EconInfo.numOfFreeLivingSpaces(city),
            EconInfo.numOfFreeWorkPlaces(city, EResources.FOOD),
            EconInfo.numOfFreeWorkPlaces(city, EResources.BRICKS)
        ],
        "Cost to build": [
            EconInfo.costToBuild(city, "house"),
            EconInfo.costToBuild(city, "farmHouse"),
            EconInfo.costToBuild(city, "brickHouse"),
        ]
    }

    st.table(data)

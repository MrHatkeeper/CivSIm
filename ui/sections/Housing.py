import streamlit as st

from civsim.City.Workplace.EResources import EResources
from civsim.Misc import EconInfo


def renderHousing(city):
    st.subheader("Housing")


    data = {
        "Type":[
            "House",
            "Farm",
            "Brick house"
        ],
        "Occupied spaces": [
            EconInfo.numOfOccupiedLivingSpaces(city),
            EconInfo.numOfOccupiedWorkPlaces(city, EResources.FOOD),
            EconInfo.numOfOccupiedWorkPlaces(city, EResources.BRICKS)
        ],

        "Free spaces": [
            EconInfo.numOfFreeLivingSpaces(city),
            EconInfo.numOfOccupiedWorkPlaces(city, EResources.FOOD),
            EconInfo.numOfOccupiedWorkPlaces(city, EResources.BRICKS)
        ]
    }

    st.table(data)
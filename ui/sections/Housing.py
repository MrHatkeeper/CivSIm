import streamlit as st
from civsim.Misc import CityInfo

def renderHousing(city):
    st.subheader("Housing")

    st.write(f"Houses: {len(city.houses)}")
    st.write(f"Free spaces: {CityInfo.numOfFreeLivingSpaces(city)}")
    st.write(f"Occupied spaces: {CityInfo.numOfOccupiedLivingSpaces(city)}")

    data = {
        "Type":[
            "House",
            "Farm",
            "Brick house"
        ],
        "Occupied spaces": [
            CityInfo.numOfOccupiedLivingSpaces(city),

        ]

        "Free spaces": [
            CityInfo.numOfFreeLivingSpaces(city),
        ]

    }
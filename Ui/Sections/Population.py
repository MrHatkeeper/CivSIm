import streamlit as st

from Civsim.City.City import City
from Civsim.Misc import PopInfo


def renderPopulation(city: City):
    st.subheader("Quantity")

    st.write(f"Total: {len(city.population)}")
    st.write(f"Adults: {len(PopInfo.getAdults(city))}")
    st.write(f"Children: {len(PopInfo.getChildren(city))}")
    st.write(f"Unemployed: {len(PopInfo.getUnemployed(city))}")
    st.write(f"Homeless: {PopInfo.numOfHomeless(city)}")
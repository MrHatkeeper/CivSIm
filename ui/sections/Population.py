import streamlit as st
from civsim.Misc import CityInfo

def renderPopulation(city):
    st.subheader("Population")

    st.write(f"Total: {len(city.population)}")
    st.write(f"Adults: {len(CityInfo.getAdults(city))}")
    st.write(f"Children: {len(CityInfo.getChildren(city))}")
    st.write(f"Unemployed: {len(CityInfo.getUnemployed(city))}")
    st.write(f"Homeless: {CityInfo.numOfHomeless(city)}")
import streamlit as st
from civsim.Misc import PopInfo


def renderPopulation(city):
    st.subheader("Quantity")

    st.write(f"Total: {len(city.population)}")
    st.write(f"Adults: {len(PopInfo.getAdults(city))}")
    st.write(f"Children: {len(PopInfo.getChildren(city))}")
    st.write(f"Unemployed: {len(PopInfo.getUnemployed(city))}")
    st.write(f"Homeless: {PopInfo.numOfHomeless(city)}")
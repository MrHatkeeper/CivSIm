import streamlit as st
from civsim.City.Workplace.EResources import EResources
from civsim.Misc import CityInfo

def renderEconomy(city):
    st.subheader("Economy")

    production = CityInfo.getProduction(city)

    st.write("### Production per year")
    st.table({
        "Food": [production[EResources.FOOD]],
        "Building resources": [production[EResources.BRICKS]],
    })

    st.write(f"Consumption: {CityInfo.getConsumption(city)}")

    st.write("### Storage")
    st.table({
        "Food": [city.storage[EResources.FOOD]],
        "Building resources": [city.storage[EResources.BRICKS]],
    })
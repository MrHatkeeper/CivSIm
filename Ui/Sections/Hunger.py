import streamlit as st

from Civsim.City.City import City
from Civsim.Misc import Metrics, EconInfo


def renderHunger(city: City):
    st.subheader("Hunger")
    st.write(f"Food consumption per year: {EconInfo.getConsumption(city)}")

    st.write(f"Average hunger: {Metrics.getAverage('hunger', city)}")
    st.write(f"Lowest hunger: {Metrics.getLowest('hunger', city)}")
    st.write(f"Highest hunger: {Metrics.getHighest('hunger', city)}")

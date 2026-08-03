import streamlit as st

from Civsim.City.City import City
from Civsim.Misc import Metrics


def renderHappiness(city: City):
    st.subheader("Happiness")

    st.write(f"Average: {Metrics.getAverage('happiness', city)}")
    st.write(f"Mean: {Metrics.getMeanHappiness(city)}")
    st.write(f"Lowest: {Metrics.getLowest('happiness', city)}")
    st.write(f"Highest: {Metrics.getHighest('happiness', city)}")

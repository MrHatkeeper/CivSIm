import streamlit as st
from civsim.Misc import CityInfo

def renderHappiness(city):
    st.subheader("Happiness")

    st.write(f"Average: {CityInfo.getAverage('happiness', city)}")
    st.write(f"Lowest: {CityInfo.getLowest('happiness', city)}")
    st.write(f"Highest: {CityInfo.getHighest('happiness', city)}")
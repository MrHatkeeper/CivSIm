import streamlit as st
from civsim.Misc import CityInfo

def renderHunger(city):
    st.subheader("Hunger")

    st.write(f"Average: {CityInfo.getAverage('hunger', city)}")
    st.write(f"Lowest: {CityInfo.getLowest('hunger', city)}")
    st.write(f"Highest: {CityInfo.getHighest('hunger', city)}")
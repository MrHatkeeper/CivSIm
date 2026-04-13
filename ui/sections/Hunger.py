import streamlit as st
from civsim.Misc import Metrics, EconInfo


def renderHunger(city):
    st.subheader("Hunger")
    st.write(f"Food consumption per year: {EconInfo.getConsumption(city)}")

    st.write(f"Average: {Metrics.getAverage('hunger', city)}")
    st.write(f"Lowest: {Metrics.getLowest('hunger', city)}")
    st.write(f"Highest: {Metrics.getHighest('hunger', city)}")
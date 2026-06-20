import streamlit as st
from Civsim.Misc import Metrics


def renderHappiness(city):
    st.subheader("Happiness")

    st.write(f"Average: {Metrics.getAverage('happiness', city)}")
    st.write(f"Lowest: {Metrics.getLowest('happiness', city)}")
    st.write(f"Highest: {Metrics.getHighest('happiness', city)}")
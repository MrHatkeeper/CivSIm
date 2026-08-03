import streamlit as st

from Civsim.City.City import City


def renderStatistics(city: City):
    """
    Slouží k vykreslení grafů
    :param city: jaké město se vykresluje
    """
    data = city.historySystem.showData()
    if len(data) == 0:
        return
    else:
        st.title("Statistics")
        st.subheader("Population graph")
        st.line_chart(data[0], x="year", y_label="Number of people")
        st.subheader("Happiness graph")
        st.line_chart(data[1], x="year", y_label="units of happiness")

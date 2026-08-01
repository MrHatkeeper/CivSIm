import streamlit as st

"""
Co chci měřit

Avg happiness
Počet lidí
Počet bezdomovců
Storage
Počet budov
Jakých budov
"""
def renderStatistics(city):
    data = city.historySystem.showData()
    if len(data) == 0:
        return
    else:
        st.title("Statistics")
        st.line_chart(data[0], x="year", y_label="Number of people")
        st.line_chart(data[1], x="year", y_label="units of happiness")


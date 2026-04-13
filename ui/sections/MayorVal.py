import streamlit as st

from civsim.City.City import City


def renderMayor(city: City):

    if city.mayor is None:
        return

    st.subheader("Mayor eval values")
    for action in city.mayor.actionValues:
        st.write(f"value of {action}: {city.mayor.actionValues[action]}")
    st.write(f"Mayor did: {city.mayor.lastAction}")
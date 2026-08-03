import streamlit as st

from Civsim.City.City import City


def renderMayor(city: City):
    """
    Vykresluje, jak vyšly hodnoty vyhodnocovacího modelu
    :param city: jaké město se vykresluje
    """
    if city.mayor is None:
        return

    st.subheader("Mayor eval values")
    for action in city.mayor.actionValues:
        st.write(f"value of {action}: {city.mayor.actionValues[action]}")
    st.write(f"Mayor's action: {city.mayor.lastAction}")

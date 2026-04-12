import streamlit as st

from ui.sections.Population import renderPopulation
from ui.sections.Housing import renderHousing
from ui.sections.Happiness import renderHappiness
from ui.sections.Hunger import renderHunger
from ui.sections.Economy import renderEconomy


def renderDashboard(gm):
    optionMan = {city.name: city for city in gm.cities}
    if "selected_city" not in st.session_state:
        st.session_state.selected_city = None

    selection = st.pills(
        "Select city:",
        options = optionMan.keys(),
        selection_mode = "single",
        default = st.session_state.selected_city
    )

    if selection is None:
        return

    if selection is not None:
        st.session_state.selected_city = selection

    city = optionMan[st.session_state.selected_city]

    st.title(f"City: {city.name}")

    renderPopulation(city)
    renderHousing(city)
    renderHappiness(city)
    renderHunger(city)
    renderEconomy(city)
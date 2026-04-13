import streamlit as st

from ui.sections.Population import renderPopulation
from ui.sections.Housing import renderHousing
from ui.sections.Happiness import renderHappiness
from ui.sections.Hunger import renderHunger
from ui.sections.Economy import renderResources
from ui.sections.MayorVal import renderMayor


def renderDashboard(gm):
    optionMan = {city.name: city for city in gm.cities}
    if "selected_city" not in st.session_state:
        st.session_state.selected_city = None


    if len(optionMan) == 0:
        return

    selection = st.pills(
        "Select city:",
        options = optionMan.keys(),
        selection_mode = "single",
        default = list(optionMan.keys())[0],
    )

    if selection is None:
        return

    if selection is not None:
        st.session_state.selected_city = selection

    city = optionMan[st.session_state.selected_city]

    st.title(f"City: {city.name}")

    renderMayor(city)
    st.write("# Population")
    col1, col2, col3 = st.columns(3, border=True)
    with col1:
        renderPopulation(city)
    with col2:
        renderHappiness(city)
    with col3:
        renderHunger(city)
    st.write("# Economy")
    renderHousing(city)
    renderResources(city)
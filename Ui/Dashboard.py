import streamlit as st

from Ui.Sections.Population import renderPopulation
from Ui.Sections.Housing import renderHousing
from Ui.Sections.Happiness import renderHappiness
from Ui.Sections.Hunger import renderHunger
from Ui.Sections.Economy import renderResources
from Ui.Sections.MayorVal import renderMayor


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

    if st.button("Save City"):
        gm.saver.exportCity(city)

    st.title(f"City: {city.name}")
    st.write(f"Year in city: {city.year}")

    if len(city.population) == 0:
        st.write(f"# City disappeared on year {city.year}")
        return

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
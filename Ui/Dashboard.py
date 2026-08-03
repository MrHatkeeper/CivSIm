import streamlit as st

from Civsim.GameMaster import GameMaster
from Ui.Sections.CityPreview import renderCityPreview


def renderDashboard(gm: GameMaster):
    """
    Vykresluje a spravuje hlavní část webového rozhraní
    :param gm: slouží pro získání seznamu měst v simulaci
    """
    citiesToSelect = {city.name: city for city in gm.cities}
    if "selected_city" not in st.session_state:
        st.session_state.selected_city = None

    if len(citiesToSelect) == 0:
        return

    selection = st.pills(
        " ",
        options=citiesToSelect.keys(),
        selection_mode="single",
        default=list(citiesToSelect.keys())[0],
    )

    if selection is None:
        return

    if selection is not None:
        st.session_state.selected_city = selection

    city = citiesToSelect[st.session_state.selected_city]

    renderCityPreview(city)

from streamlit import sidebar

from civsim.City.Workplace.EResources import EResources
from civsim.GameMaster import GameMaster
import streamlit as st

from civsim.Misc import CityInfo
from ui.Dashboard import renderDashboard
from ui.SideBar import SideBar

if __name__ == "__main__":
    if "gm" not in st.session_state:
        st.session_state.gm = GameMaster()

    gm = st.session_state.gm

    st.write("# Year: ", str(gm.year))

    SideBar(gm)
    renderDashboard(gm)
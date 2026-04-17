from time import sleep

from civsim.GameMaster import GameMaster
import streamlit as st

from ui.Dashboard import renderDashboard
from ui.SideBar import SideBar


if __name__ == "__main__":
    if "gm" not in st.session_state:
        st.session_state.gm = GameMaster()


    gm = st.session_state.gm


    st.write("# Year: ", str(gm.year))

    SideBar(gm)

    renderDashboard(gm)

    if gm.isRunning:
        gm.moveOneYear()
        sleep(gm.getSpeed())
        st.rerun()
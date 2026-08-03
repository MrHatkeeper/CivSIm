from time import sleep

from Civsim.GameMaster import GameMaster
import streamlit as st

from Ui.Dashboard import renderDashboard
from Ui.SideBar import SideBar

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

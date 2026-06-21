from io import StringIO

import streamlit as st
from numpy.ma.extras import unique

from Civsim.SaveManager.Saver import Saver


class SideBar:
    def __init__(self, gm):
        self.gm = gm
        self.render()

    def render(self):
        mainSettings = st.sidebar.container()

        mainSettings.title("Simulation Control")

        with mainSettings:
            if not self.gm.isRunning:
                if st.button("Run simulation", unique(True), disabled=len(self.gm.cities) == 0):
                    self.gm.isRunning = True
                    st.rerun()
            else:
                if st.button("Pause simulation", unique(True)):
                    self.gm.isRunning = False
                    st.rerun()
            uploadedSave = st.file_uploader("Load saved city", accept_multiple_files=False, type="json")
            if st.button("Load saved city"):
                self.gm.loader.loadCity(uploadedSave)
                st.rerun()

            st.subheader("Simulation speed")
            self.gm.speedMultiplier = st.slider("Years per second", min_value=1, max_value=6, value=1, step=1)

            st.subheader("Create new simulation")

            numOfStartCities = st.number_input(
                "Start cities",
                min_value=1,
                max_value=10,
                value=1
            )

            if st.button("Create Simulation"):
                self.gm.crateSimulation(numOfStartCities)
                st.rerun()

            if st.button("Next year"):
                self.gm.moveOneYear()
                st.rerun()
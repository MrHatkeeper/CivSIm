import streamlit as st


class SideBar:
    def __init__(self, gm):
        self.gm = gm
        self.render()

    def render(self):
        st.sidebar.title("Simulation Control")

        mainSettings = st.sidebar.container()

        with mainSettings:
            st.subheader("Create new simulation")

            numOfStartCities = st.number_input(
                "Start cities",
                min_value=1,
                max_value=10,
                value=1
            )
            if st.button("Start simulation"):
                self.gm.startSimulation(numOfStartCities)
                st.rerun()

            if st.button("Next year"):
                self.gm.moveOneYear()
                st.rerun()
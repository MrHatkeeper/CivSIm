import streamlit as st


class SideBar:
    def __init__(self):
        with st.sidebar:
            st.text("Create new simulation")
            setup = st.columns(2)
            setup[0].subheader("Number of starting cities")
            numOfStartCities = st.number_input("Start cities", min_value=1, max_value=10, value=1)
            if st.button("Start simulation"):
                st.session_state.gm.startSimulation(numOfStartCities)
            if st.button("Move one year"):
                st.session_state.gm.moveOneYear()
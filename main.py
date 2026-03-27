from civsim.GameMaster import GameMaster
import streamlit as st

if __name__ == '__main__':
    gm = GameMaster()
    if "gm" not in st.session_state:
        st.session_state.gm = GameMaster()

    with st.sidebar:
        st.text("Create new simulation")
        setup = st.columns(2)
        setup[0].subheader("Number of starting cities")
        numOfStartCities = st.number_input("Start cities", min_value=1, max_value=10, value=1)
        if st.button("Start simulation"):
            st.session_state.gm.startSimulation(numOfStartCities)
        if st.button("Show simulation"):
            st.session_state.gm.af()
        st.text(st.session_state.gm.a)

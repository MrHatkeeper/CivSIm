import streamlit as st
from Civsim.City.Workplace.EResources import EResources
from Civsim.Config import Config
from Civsim.Misc import EconInfo


def renderResources(city):
    production = EconInfo.getProduction(city)
    data = {
        "Type": [
            "Food",
            "Building resources",
        ],
        "Production per one worker": [Config.PROD_RATIO.value] * len(production),
        "Production per year": list(production.values()),
        "In storage": [round(i, 1) for i in city.storage.values()]
    }
    st.subheader("Production")

    st.table(data)

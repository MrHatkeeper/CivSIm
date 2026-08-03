import streamlit as st

from Civsim.City.City import City
from Civsim.Config import Config
from Civsim.Misc import EconInfo


def renderResources(city: City):
    """
    Vykreslení stavu skladu města
    :param city:
    """
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

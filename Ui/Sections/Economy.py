import streamlit as st
from Civsim.City.Workplace.EResources import EResources
from Civsim.Config import Config
from Civsim.Misc import EconInfo


def renderResources(city):
    production = EconInfo.getProduction(city)
    st.subheader("Production")
    #print(production)
    data = {
        "Type": [
            "Food",
            "Building resources",
        ],
        "Production per one worker":[
            Config.PROD_RATIO.value,
            Config.PROD_RATIO.value
        ],
        "Production per year": [
            production[EResources.FOOD],
            production[EResources.BRICKS]
        ],
        "In storage": [
            round(city.storage[EResources.FOOD], 1),
            round(city.storage[EResources.BRICKS], 1),
        ]
    }

    st.table(data)

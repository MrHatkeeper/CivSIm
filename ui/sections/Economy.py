import streamlit as st
from civsim.City.Workplace.EResources import EResources
from civsim.Misc import EconInfo

def renderResources(city):

    production = EconInfo.getProduction(city)

    st.subheader("Production")
    data = {
        "Type":[
            "Food",
            "Building resources",
        ],
        "Production per year":[
            production[EResources.FOOD],
            production[EResources.BRICKS]
        ],
        "In storage":[
            city.storage[EResources.FOOD],
            city.storage[EResources.BRICKS],
        ]
    }

    st.table(data)
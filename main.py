from streamlit import sidebar

from civsim.City.Workplace.EResources import EResources
from civsim.GameMaster import GameMaster
import streamlit as st

from civsim.Misc import CityInfo
from ui.SideBar import SideBar

if __name__ == '__main__':
    if "gm" not in st.session_state:
        st.session_state.gm = GameMaster()

    sidebar = SideBar()

    optionMap = {}
    if st.session_state.gm is not None:
        st.write(f"# Year {st.session_state.gm.year}")
    for i in st.session_state.gm.cities:
        optionMap[i.name] = i
    selection = st.pills(
        "Select city:",
        options=optionMap.keys(),
        selection_mode="single",
    )

    if selection is not None:
        selectedCity = optionMap[selection]
        f'''
        # City name: {selectedCity.name}
        ### Population: {len(selectedCity.population)}
        Adults: {len(CityInfo.getAdults(selectedCity))} \n
        Unemployed: {len(CityInfo.getUnemployed(selectedCity))} \n
        Children: {len(CityInfo.getChildren(selectedCity))} \n
        ### Number of houses: {len(selectedCity.houses)} \n
        Free living spaces: {CityInfo.numOfFreeLivingSpaces(selectedCity)} \n
        Occupied living spaces: {CityInfo.numOfOccupiedLivingSpaces(selectedCity)} \n
        Homeless: {CityInfo.numOfHomeless(selectedCity)} \n
        ### Happiness
        Average happiness: {CityInfo.getAverage("happiness", selectedCity)} \n
        Lowest happiness: {CityInfo.getLowest("happiness", selectedCity)} \n
        Highest happiness: {CityInfo.getHighest("happiness", selectedCity)} \n
        ### Hunger
        Average hunger: {CityInfo.getAverage("hunger", selectedCity)} \n
        Lowest hunger: {CityInfo.getLowest("hunger", selectedCity)} \n
        Highest hunger: {CityInfo.getHighest("hunger", selectedCity)} \n
        
        ### Production per year
        | Food | Building resources 
        --- | ---
        {CityInfo.getProduction(selectedCity)[EResources.FOOD]}| {CityInfo.getProduction(selectedCity)[EResources.BRICKS]}
        
        ### Food consumption: {CityInfo.getConsumption(selectedCity)}
         
        ### Storage
        | Food | Building resources 
        --- | ---
        {selectedCity.storage[EResources.FOOD]} | {selectedCity.storage[EResources.BRICKS]} 
        
        '''
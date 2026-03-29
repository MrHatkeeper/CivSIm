from civsim.City.Workplace.EResources import EResources
from civsim.GameMaster import GameMaster
import streamlit as st

from civsim.Misc import CityInfo

if __name__ == '__main__':
    if "gm" not in st.session_state:
        st.session_state.gm = GameMaster()

    with st.sidebar:
        st.text("Create new simulation")
        setup = st.columns(2)
        setup[0].subheader("Number of starting cities")
        numOfStartCities = st.number_input("Start cities", min_value=1, max_value=10, value=1)
        if st.button("Start simulation"):
            st.session_state.gm.startSimulation(numOfStartCities)

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
        #### Adults: {len(CityInfo.getAdults(selectedCity))}
        #### Unemployed: {len(CityInfo.getUnemployed(selectedCity))}
        ### Number of houses: {len(selectedCity.houses)} \n
        #### Free living spaces: {CityInfo.numOfFreeLivingSpaces(selectedCity)}
        #### Occupied living spaces: {CityInfo.numOfOccupiedLivingSpaces(selectedCity)}
        #### Homeless: {CityInfo.numOfHomeless(selectedCity)}
        ### Average happiness: {CityInfo.getAverage("happiness", selectedCity)}
        #### Lowest happiness: {CityInfo.getLowest("happiness", selectedCity)}
        #### Highest happiness: {CityInfo.getHighest("happiness", selectedCity)}
        ### Average hunger: {CityInfo.getAverage("hunger", selectedCity)}
        #### Lowest hunger: {CityInfo.getLowest("hunger", selectedCity)}
        #### Highest hunger: {CityInfo.getHighest("hunger", selectedCity)}
        
        ### Production per year
        | Food | Building resources 
        --- | ---
        {CityInfo.getProduction(selectedCity)[EResources.FOOD]}| {CityInfo.getProduction(selectedCity)[EResources.BRESOURCES]}
        
        ### Food consumption: ...
         
        ### Storage
        | Food | Building resources 
        --- | ---
        {selectedCity.storage[EResources.FOOD]} | {selectedCity.storage[EResources.BRESOURCES]} 
        
        '''
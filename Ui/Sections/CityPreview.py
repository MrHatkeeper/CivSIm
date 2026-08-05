import streamlit as st

from Civsim.City.City import City
from Civsim.SaveManager.Saver import exportCity
from Ui.Sections.Economy import renderResources
from Ui.Sections.Happiness import renderHappiness
from Ui.Sections.Housing import renderHousing
from Ui.Sections.Hunger import renderHunger
from Ui.Sections.MayorOverview import renderMayor
from Ui.Sections.Population import renderPopulation
from Ui.Sections.Statistics import renderStatistics


def renderCityPreview(city: City):
    """
    Vykreslení náhledu města
    :param city: jaké město se vykresluje
    """
    if st.button("Save City"):
        exportCity(city)

    st.title(f"City: {city.name}")
    st.write(f"Year in city: {city.year}")

    if len(city.population) == 0:
        st.write(f"# City disappeared on year {city.year}")
        return

    renderMayor(city)
    st.write("# Population")
    col1, col2, col3 = st.columns(3, border=True)
    with col1:
        renderPopulation(city)
    with col2:
        renderHappiness(city)
    with col3:
        renderHunger(city)
    st.write("# Economy")
    renderHousing(city)
    renderResources(city)
    renderStatistics(city)

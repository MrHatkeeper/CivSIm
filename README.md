# Simulace vývoje města

## O co se jedná

CimvSim je jednoduchá simulace města založená na radosti obyvatel, možnosti bydlení a dostupnosti jídla pomocí
vyhodnocovacího modelu.

## Cíl projektu

- Simulovat růst počtu obyvatel.
- Zkoumat, jak se při různých hodnotách v modelu mění jeho rozhodování.

## Návrh architektury

Projekt je rozdělen do několika podadresářů. Samotná funkcionalita města je rozdělena do systémů, aby se předešlo
jednomu přehlcenému souboru. Podobným způsobem je vedeno vykreslování, které je taktéž rozděleno do sekcí.

- `CimvSim/` - obsahuje kód simulace.
    - `City/`- obsahuje kód pro funkcli města.
        - `Systems/` - obsahuje jednotné systémy města.
        - `Workplace/`- obsahuje kód pro výpočet surovin ve skladu.
    - `Human/` - obsahuje kód pro obyvatele a výpočet radosti.
    - `Mayor/` - obsahuje kód vyhodnocovacího modelu.
    - `Misc/` - pomocné funkce pro získávání dat,
    - `SaveManager/` - kód pro načítání a ukládání historie města.
- `Saves/` - složka pro uložené stavy měst.
- `Ui/` - vykreslování dat na uživatelského rozhraní.
    - `Sections/` - sekce pro vykreslení.
- `main.py` - hlavní soubor, který slouží k zapnutí.

## Použití

### Zapnutí aplikace

1. Projekt se zapne pomocí `streamlit run main.py`.
2. Následně se otevře prohlížečové rozhraní.
3. V sekci **Create new simulation** si uživatel nakliká, kolik chce simulovat měst zároveň.
4. Simulace se automaticky spustí.

### Pozastavení simulace
1. Uživatel klikne v sekci **Simulation Control** na tlačítko **Pause simulation**.
2. Pro zapnutí klikne na tlačítko **Run simulation**

###  Uložení stavu města
1. Uživatel si v nabídce měst rozklikne město, které chce uložit.
2. Pod nabídkou klikne na tlačítko **Save City**
3. Město se uloží do složky `Saves/`

### Načtení uloženého města
1. Uživatel klikne v sekci **Load saved city** na tlačítko **Browse files**.
2. Uživateli se otevře prohlížeč souborů, kde si může vybrat, jaké město chce načíst.
3. Uživatel vybere soubor.
4. Pomocí následného kliknutí na tlačítko **Load saved city** se načte vybrané město.

### Instalace

> Vytvoření a vybrání virtuálního prostředí (pokud již neexistuje):
> - `python -m venv venv`
> - `source venv/bin/activate`

> Instalace potřebných knihoven:
> - `pip install -r requirements.txt`

## Požadavky

- Python 3.14+
- Balíčky v `requirements.txt`
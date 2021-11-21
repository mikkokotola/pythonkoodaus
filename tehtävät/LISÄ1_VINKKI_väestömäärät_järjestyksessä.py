from time import sleep

# Tässä luetaan tietoa JSON-tiedostosta - älä muuta tätä
import json
with open('./data/maatiedot.json', encoding='utf-8') as json_file:
    maat = json.load(json_file)

# TEHTÄVÄ: tulosta kaikkien euroopan maiden väestömäärät järjestyksessä suurimmasta pienimpään
# Kirjoita koodia tähän

# Määritellään apufunktio
def valitse_väestömäärä(maa):
    return  # Palauta tässä maan ominaisuus väestömäärä

# Tässä lajitellaan maat käyttäen funktiota valitse_väestömäärä
maat.sort(key=valitse_väestömäärä, reverse=True)

# Tulosta maat kuten edellisessä tehtävässä

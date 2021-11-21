# Tässä luetaan tietoa JSON-tiedostosta - älä muuta tätä
import json
with open('./data/maatiedot.json', encoding='utf-8') as json_file:
    maat = json.load(json_file)

# VAIHE 1: kysy käyttäjältä maan nimeä ja tallenna se muuttujaan etsittävä_maa


# VAIHE 2: käy for-silmukalla läpi kaikki maat. Jos maan nimi on sama kuin etsittävä_maa, tulosta
# maan nimi ja väestömäärä.

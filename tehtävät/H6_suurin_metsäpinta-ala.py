# Tässä luetaan tietoa JSON-tiedostosta - älä muuta tätä
import json
with open('./data/maatiedot.json', encoding='utf-8') as json_file:
    maat = json.load(json_file)

# TEHTÄVÄ: käy läpi maat ja etsi se, jolla on suurin metsäpinta-ala
# Täytä koodia tähän. Ota mallia pisimmän oppilaan etsimisestä.


# Tässä luetaan tietoa JSON-tiedostosta - älä muuta tätä
import json
with open('./data/maatiedot.json', encoding='utf-8') as json_file:
    maat = json.load(json_file)

# TEHTÄVÄ: Kysy käyttäjältä maan nimeä, ja näytä sitten kuinka suuri osa (%) kyseisen maan pinta-alasta on metsää 
# Ota tarvittaessa mallia tehtävästä H3 väestömäärä
# Täytä koodia tähän


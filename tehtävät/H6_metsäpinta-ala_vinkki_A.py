# Tässä luetaan tietoa JSON-tiedostosta - älä muuta tätä
import json
with open('./data/maatiedot.json', encoding='utf-8') as json_file:
    maat = json.load(json_file)

# TEHTÄVÄ: Kysy käyttäjältä maan nimeä, ja näytä sitten kuinka suuri osa (%) kyseisen maan pinta-alasta on metsää 
# Ota tarvittaessa mallia tehtävästä H3 väestömäärä
# Täytä koodia tähän

# 1. Kysy käyttäjältä etsittävän maan nimi ja tallenna se muuttujaan etsittävä_maa
etsittävä_maa =

# Alustetaan muuttujat maanimi ja metsäpintaala. Laitetaan niille arvoksi None (tyhjä arvo).
maanimi = None
metsäpintaala = None

# 2. Käy läpi kaikki maat for-silmukalla

# 3. Silmukan sisällä, jos maan nimi on etsittävä_maa, tallenna maan nimi muuttujaan maanimi ja metsäpinta-ala
# muuttujaan metsäpintaala


if (maanimi and metsäpintaala):
    print (f'Maan {maanimi} metsäpinta-ala on {metsäpintaala} % maapinta-alasta.')
else:
    print (f'Maata tai arvoa ei löytynyt nimellä {etsittävä_maa}.')


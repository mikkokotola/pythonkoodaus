import io
import json
import requests
from PIL import Image
from random import choice

# Tässä luetaan tietoa JSON-tiedostosta - älä muuta tätä
with open("./data/maatiedot.json", encoding="utf-8") as json_file:
    maat = json.load(json_file)

maa = next((x for x in maat if x["nimi"] == "Suomi"), None)

# Arvotaan satunnainen maa listasta
# TEHTÄVÄ: arvo satunnainen maa listasta maat ja tallenna se muuttujaan maa

# Haetaan lipun kuva arvotun maan lippuosoitteesta ja näytetään lippu pelaajalle - älä muuta tätä koodia
lippuosoite = maa["lippu"]
response = requests.get(lippuosoite)
image_bytes = io.BytesIO(response.content)
img = Image.open(image_bytes)
img.show()

# TEHTÄVÄ: pyydä käyttäjää arvaamaan maa ja tallenna se muuttujaan arvaus. Jos arvaus on oikein,
# näytä viesti "Hienoa, oikein!". Jos arvaus on väärin, näytä viesti, joka kertoo oikean vastauksen
# Esimerkiksi "Ou nou, väärin! Oikea vastaus oli Ruotsi."

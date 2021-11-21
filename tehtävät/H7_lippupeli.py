import json
import requests
import time
from PIL import Image
import io

# Tässä luetaan tietoa JSON-tiedostosta - älä muuta tätä
with open('./data/maatiedot.json', encoding='utf-8') as json_file:
    maat = json.load(json_file)

# Arvotaan satunnainen maa listasta
from random import choice
maa = choice(maat)

print()
print("** Tervetuloa lippupeliin! **")
print()
print("Näet kohta jonkun Euroopan maan lipun. Kun sinulla on arvaus maasta, sulje ikkuna ja syötä maan nimi.")
time.sleep(5)

# Näytetään pelaajalle maan lippu
lippuosoite = maa['lippu']
response = requests.get(lippuosoite)
image_bytes = io.BytesIO(response.content)
img = Image.open(image_bytes)
img.show()


# TEHTÄVÄ: pyydä käyttäjää arvaamaan maa ja tallenna se muuttujaan arvaus. Jos arvaus on oikein,
# näytä viesti "Hienoa, oikein!". Jos arvaus on väärin, näytä viesti, joka kertoo oikean vastauksen
# Esimerkiksi "Ou nou, väärin! Oikea vastaus oli Ruotsi."

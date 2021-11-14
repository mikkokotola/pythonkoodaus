from time import sleep

# Tässä luetaan tietoa JSON-tiedostosta - älä muuta tätä
import json
with open("./data/oppilaat.json", encoding="utf-8") as json_file:
    # Luetaan lista oppilaista muuttujaan nimeltä "oppilaat"
    oppilaat = json.load(json_file)

# Tässä otetaan listalta yksi oppilas kerrallaan ja tehdään jotain kyseisen oppilaan tiedoilla.
# For-silmukka käy käpi kaikki oliot listalla.
for oppilas in oppilaat:
    nimi = oppilas['nimi']
    pituus = oppilas['pituus']
    print (f"Oppilas: {nimi}, pituus {pituus} cm")
    # Odotetaan sekunti ennen kuin jatketaan
    sleep(1.0)

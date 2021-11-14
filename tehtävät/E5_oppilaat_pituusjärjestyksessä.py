from time import sleep

# Tässä luetaan tietoa JSON-tiedostosta - älä muuta tätä
import json
with open("./data/oppilaat.json", encoding="utf-8") as json_file:
    # Luetaan lista oppilaista muuttujaan nimeltä "oppilaat"
    oppilaat = json.load(json_file)

# Järjestetään oppilaat pituusjärjestykseen
# Määritellään apufunktio, joka palauttaa sille annetun oppilaan pituuden
def valitse_pituus(oppilas):
    return oppilas['pituus']

oppilaat.sort(key=valitse_pituus, reverse=True)

# Tässä otetaan listalta yksi oppilas kerrallaan ja tehdään jotain kyseisen oppilaan tiedoilla.
# For-silmukka käy käpi kaikki oliot listalla.
for oppilas in oppilaat:
    nimi = oppilas['nimi']
    pituus = oppilas['pituus']
    print (f"Oppilas: {nimi}, pituus {pituus} cm")
    # Odotetaan puoli sekuntia ennen kuin jatketaan
    sleep(0.5)

# Tässä luetaan tietoa JSON-tiedostosta - älä muuta tätä
import json
with open("./data/oppilaat.json", encoding="utf-8") as json_file:
    # Luetaan lista oppilaista muuttujaan nimeltä "oppilaat"
    oppilaat = json.load(json_file)

# Alustetaan apumuuttujat.
pisin_oppilas = None
suurin_pituus = 0
laskuri = 0

# Tässä otetaan listalta yksi oppilas kerrallaan ja tehdään jotain kyseisen oppilaan tiedoilla.
# For-silmukka käy käpi kaikki oliot listalla.

for oppilas in oppilaat:
    # Varmistetaan, että oppilaalla on pituus. Jos ei, jatketaan suoraan seuraavaan oppilaaseen.
    if not (oppilas['pituus']):
        continue
    
    # Lasketaan kuinka monta oppilasta on käsitelty
    laskuri = laskuri + 1

    # Tarkastetaan, onko nyt käsiteltävä oppilas pidempi kuin tähän mennessä pisin. Jos on, tallennetaan
    # uuden pisimmän oppilaan tiedot.
    if (oppilas['pituus'] > suurin_pituus):
        suurin_pituus = oppilas['pituus']
        pisin_oppilas = oppilas['nimi']

# Tulostetaan tulokset
print (f"Pisin oppilas on {pisin_oppilas} ({suurin_pituus} cm)")
print (f"Käsitelty {laskuri} oppilasta")
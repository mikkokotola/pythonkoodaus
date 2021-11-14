# Tässä luetaan tietoa JSON-tiedostosta - älä muuta tätä
import json
with open("./data/oppilaat.json", encoding="utf-8") as json_file:
    # Luetaan lista oppilaista muuttujaan nimeltä "oppilaat"
    oppilaat = json.load(json_file)

# VAIHE 1: kysytään käyttäjältä oppilaan nimeä ja tallennetaan se muuttujaan etsittävä_nimi
etsittävä_nimi = input("Kuka oppilas? ")

# Alustetaan apumuuttuja, jolla tarkastetaan, löytyikö oppilasta annetulla nimellä
löytyi = False

# VAIHE 2: käydään for-silmukalla läpi oppilaita. Jos oppilaan nimi on sama kuin etsittävä_nimi, 
# tulostetaan oppilaan tiedot.
for oppilas in oppilaat:
    if oppilas['nimi'] == etsittävä_nimi:
        print ('Oppilas löytyi!')
        print (f"Oppilas: {oppilas['nimi']}, ikä: {oppilas['ikä']}, lempiväri {oppilas['lempiväri']}, pituus {oppilas['pituus']}")
        # Merkataan, että oppilas löytyi
        löytyi = True
        # Lopetetaan silmukan läpi käynti: löysimme jos etsimämme oppilaan, loppuja ei tarvitse käsitellä
        break

# Jos oppilasta ei löytynyt, kerrotaan se käyttäjälle
if not (löytyi):
    print("Voi rähmä! Annetulla nimellä ei löytynyt oppilasta.")



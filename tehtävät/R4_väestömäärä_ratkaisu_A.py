# Tässä luetaan tietoa JSON-tiedostosta - älä muuta tätä
import json
with open("./data/maatiedot.json", encoding="utf-8") as json_file:
    maat = json.load(json_file)

# VAIHE 1: kysy käyttäjältä maan nimeä ja tallenna se muuttujaan etsittävä_maa
etsittävä_maa = input("Mikä maa? ")

# VAIHE 2: käy for-silmukalla läpi kaikki maat. Jos maan nimi on sama kuin etsittävä_maa, tulosta
# maan nimi ja väestömäärä.
löytyi = False

for maa in maat:
    if maa["nimi"] == etsittävä_maa:
        maanimi = maa["nimi"]
        arvo = maa["väestömäärä"]
        print (f"Maan {maanimi} väestömäärä on {arvo}.")
        löytyi = True
        break

if not löytyi:
    print(f"Däng! Maata nimellä {etsittävä_maa} ei löytynyt!")
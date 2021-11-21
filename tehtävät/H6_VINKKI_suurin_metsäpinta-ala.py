# Tässä luetaan tietoa JSON-tiedostosta - älä muuta tätä
import json
with open('./data/maatiedot.json', encoding='utf-8') as json_file:
    maat = json.load(json_file)

# TEHTÄVÄ: käy läpi maat ja etsi se, jolla on suurin metsäpinta-ala
# Täytä koodia tähän. Ota mallia pisimmän oppilaan etsimisestä.

suurin_maa = None
suurin_arvo = 0
laskuri = 0

for maa in maat:
    # Tarkasta, että maalla on metsäpinta-ala. Jos ei, jatka seuraavaan maahan.

    # Kasvata laskuria

    # Jos nyt käsiteltävän maan metsäpinta-ala on suurempi kuin tähän mennessä suurin arvo, päivitä suurin_arvo ja suurin_maa

print (f"Suhteessa eniten metsäpinta-alaa on maassa {suurin_maa} ({suurin_arvo} %)")
print (f"Käsitelty {laskuri} maata")
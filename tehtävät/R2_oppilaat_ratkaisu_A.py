# Tässä luetaan tietoa JSON-tiedostosta - älä muuta tätä
import json
with open("./data/oppilaat.json", encoding="utf-8") as json_file:
    # Luetaan lista oppilaista muuttujaan nimeltä "oppilaat"
    oppilaat = json.load(json_file)

# Tässä otetaan listalta yksi oppilas kerrallaan ja tehdään jotain kyseisen oppilaan tiedoilla.
# For-silmukka käy käpi kaikki oliot listalla.
for oppilas in oppilaat:
    print ("Oppilas:", oppilas["nimi"] , ", ikä:" ,  oppilas["ikä"] , ", lempiväri: ", oppilas["lempiväri"])

# TEHTÄVÄ: Muuta ohjelmaa siten, että jokaisesta oppilaasta tulostaan nimen lisäksi
# myös ikä ja lempiväri. 
# Esimerkkitulostus yhdelle oppilaalle: 
# Oppilas: Jarkko, ikä: 11, lempiväri: sininen
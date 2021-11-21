from time import sleep

# Tässä luetaan tietoa JSON-tiedostosta - älä muuta tätä
import json
with open('./data/maatiedot.json', encoding='utf-8') as json_file:
    maat = json.load(json_file)

# TEHTÄVÄ: tulosta kaikkien euroopan maiden väestömäärät aina puolen sekunnin välein
# Kirjoita koodia tähän

for maa in maat:
    maanimi = maa['nimi']
    väestömäärä = maa['väestömäärä']
    print (f'Maan {maanimi} väestömäärä on {väestömäärä}')
    sleep(0.5)
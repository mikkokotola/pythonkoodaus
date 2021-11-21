import requests
import json

# Haetaan internetistä tiedot tällä hetkellä avaruudessa olevista astronauteista.
response = requests.get("http://api.open-notify.org/astros.json")
astronautit = response.json()["people"]
print(astronautit)

# Tee ohjelma, joka tulostaa jokaisen avaruudessa olevan astronautin nimen ja aluksen. Astronauttien tiedot tulee tulostaa yksi kerrallaan puolen sekunnin välein.

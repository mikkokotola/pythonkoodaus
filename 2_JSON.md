# Eurooppa-koodaus: JSON
Mikko Kotola  
Syksy 2021

## Hae tiedot
- Tätä ja seuraavaa osiota varten tarvitsemme tiedostoja. Seuraa näitä ohjeita:
    1. Mene selaimella osoitteeseen https://github.com/mikkokotola/pythonkoodaus
    2. Paina vihreää nappia "Code" ja sitten "Download ZIP"
    ![Lataa materiaali](./pics/Lataa_materiaali.png)
    
    3. Tallenna tiedosto koneellesi oletuskansioon 
    4. Avaa tiedostonhallinta, ja mene tuohon samaan kansioon
    5. Paina tiedoston nimen päällä hiiren oikeaa nappia, ja valitse "Pura kaikki"

## Avaa koodieditori
- Käytämme koodaukseen tästä eteenpäin Visual Studio code -sovellusta. Tee näin:
    1. Avaa koneellasi ohjelma "Visual Studio Code"
    2. Valitse ylävalikosta "File" ja sen alta "Open Folder"
    3. Valitse kansio "tehtävät" lataamasi kansion alta
    4. Valitse vasemmasta reunasta tehtävät -> data -> oppilaat.json
    5. Sinulla pitäisi nyt näkyä näytölläsi tiedosto, jossa on tietoa oppilaista

## Yksinkertainen JSON: oppilaat
- Mikä on JSON? JavaScript Object Notation. Käytännössä koneluettava tiedon tallennusmuoto. Tietoa, jota tietokoneella on helppo lukea.
- Yksinkertainen JSON: katsotaan oppilaat.jsonia
    - Oliot: {}
    - Avain-arvo-pareja. Avain on aina lainausmerkkien välissä.
    - Arvo on yleensä numeerinen, merkkijono tai null (tyhjä arvo)
    - Lista olioita: []

### Kysymys 1: Mikä on Pekan lempiväri?
### Kysymys 2: Kuinka pitkä Reetta on?

Vastaa kysymyksiin 1 ja 2 osoitteessa: https://forms.office.com/r/NdK3fVtLtz

Seuraavia tehtäviä varten, muokkaa tiedostoa data/oppilaat_vastaus.json (älä muokkaa oppilaat.jsonia, tarvitsemme sitä jatkossa).
### Kysymys 3: Kaikki oppilaat ovat luokalla 5A. Lisää kaikille oppilaille oppilaat_vastaus.json-tiedostoon tieto luokasta.
### Kysymys 4: Koodausryhmään tulee uusi oppilas, Reino. Reino on 12-vuotias, 143 cm pitkä, pitää mustasta ja on 5F-luokalla. Lisää hänet oppilaat_vastaus.json-tiedostoon. 

Näytä vastauksesi (oppilaat_vastaus.json) opettajalle.

## Monimutkaisempi JSON: Euroopan maiden tiedot
- Avaa nyt tiedosto tehtävät/data/maatiedot.json ja vastaa seuraaviin kysymyksiin.

### Kysymys 5: Mikä on Kroatian väestömäärä?
### Kysymys 6: Kuinka monta prosenttia Monacon pinta-alasta on metsää?
### Kysymys 7: Mene selaimella Albanian lipun verkko-osoitteeseen. Mitä värejä lipussa on?

Vastaa kysymyksiin 5-7 osoitteessa: https://forms.office.com/r/mtGi6u2RGp

## Lisätehtäviä
### Harry Potter API
Mene selaimellasi seuraavaan osoitteeseen: http://hp-api.herokuapp.com/api/characters/house/gryffindor. Sivu sisältää JSON-muodossa tietoja Tylypahkan Rohkelikko-tuvan (Gryffindor) oppilaista englanniksi. Tutki tiedostoa selaimessa tai tallenna tiedosto koneellesi ja avaa se Visual Studio Codessa. Helpoiten tiedoston tallentaminen onnistuu seuraavasti: i) Selaimessa paina Ctrl + A valitaksesi kaikki teksti; ii) Paina Ctrl + C kopioidaksesi kaikki teksti; iii) Luo uusi tiedosto Visual Studio Codessa (File -> New file); iv) Liitä kopioimasi teksti painamalla Ctrl + V; v) Muotoile JSON painamalla Alt + Shift + F. Vastaa seuraaviin kysymyksiin.

### Kysymys 8: Mikä on Ron Weaslya näytelleen näyttelijän (actor) nimi?
### Kysymys 9: Mikä on Ginny Weasleyn patronus-eläin? 

Vastaa lisätehtäviin 8-9 osoitteessa: https://forms.office.com/r/9ZZEzUv22F
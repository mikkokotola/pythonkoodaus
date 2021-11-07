# Eurooppa-koodaus: Tehtäviä Euroopan maiden tiedoilla
Mikko Kotola  
Syksy 2021

## Koneelle vaadittavat ohjelmistot:
- Visual Studio Code + Python extension (Microsoft)
- Python 3:n viimeisin versio (nyt 3.9)

## Ohjeet
- Tehtävät ja esimerkkiohjelmat ovat kansiossa /tehtävät
- Osiossa edetään pääosin ensin käymällä yhdessä läpi esimerkkiohjelmia, jotka liittyvät oppilaiden tietoihin (/data/oppilaat.json), ja sitten rakentamalla idealtaan samanlaisia ohjelmia, jotka liittyvät Euroopan maiden tietoihin (/data/maatiedot.json).
- Tehtäville ei ole automaattista palautusta ja tarkastusta: ne suoritetaan näyttämällä toimiva ohjelma opettajalle ja merkkaamalla tehtävä tehdyksi listaan (taululle)

## Tehtävät
### H1 Silmukka
*Esimerkki: E1.1_listat ja E1.2_silmukka*  

Uudet aiheet:
- Lista
- For-silmukka
- Koodin ajaminen ja debuggaaminen

Tässä tehtävässä on kaksi osaa:
  - käy läpi oppiaineet yksi kerrallaan for-silmukalla ja tulosta oppiaineen nimi silmukan sisällä
  - lisää oppiaineiden listaan kaksi muuta valitsemaasi oppiainetta ja tulosta kaikkien oppiaineiden nimet kuten edellä

Ohjelman esimerkkituloste:
```
Äikkä
Matikka
Liikunta
Ympäristöoppi
Historia
Käsityöt
```

### H2 Oppilaat
*Esimerkki: esimerkki on tehtäväpohjassa H2*

Uudet aiheet:
- Tiedoston lukeminen

Muokkaa tehtäväpohjassa annettua koodia siten, että se tulostaa jokaisen oppilaan nimen, iän ja lempivärin. Data oppilaista on tiedostossa /data/oppilaat.json. 

Ohjelman esimerkkituloste:
```
Oppilas: Jarkko, ikä: 11, lempiväri: sininen
Oppilas: Liisa, ikä: 13, lempiväri: keltainen
...
```

### H3 Väestömäärä
*Esimerkki: E3_etsi_oppilas*  

Tee ohjelma, joka kysyy käyttäjältä maan nimeä, ja näyttää sitten kyseisen maan väestömäärä. Data euroopan maiden väestömääristä on tiedostossa /data/maatiedot.json. 

Ohjelman esimerkkituloste:
```
Mikä maa? Suomi
Maan Suomi väestömäärä on 5530719.
```

### H4 Kaikki väestömäärät
*Esimerkki: E4_kaikki_oppilaat*  

Uudet aiheet:  
- Odottaminen (sleep)

Tee ohjelma, joka tulostaa kaikkien Euroopan maiden väestömäärät. Tee tulostus siten, että uusi maa tulostetaan aina puolen sekunnin välein. Data euroopan maiden väestömääristä on tiedostossa /data/maatiedot.json. Maiden ei tarvitse olla suuruusjärjestyksessä. 

Ohjelman esimerkkituloste:
```
...
Maan Serbia väestömäärä on 6908224
Maan Slovakia väestömäärä on 5458827
Maan Slovenia väestömäärä on 2100126
...
```
### H5 Väestömäärät järjestyksessä
*Esimerkki: E3_oppilaat_pituusjärjestyksessä*  

Uudet aiheet:  
- Funktio
- Lajittelu

Tee ohjelma, joka tulostaa kaikkien Euroopan maiden väestömäärät järjestyksessä pienimmästä suurimpaan. Data euroopan maiden väestömääristä on tiedostossa /data/maatiedot.json. Ohjelman esimerkkituloste:
```
...
Maan Liechtenstein väestömäärä on 38137
Maan San Marino väestömäärä on 33938
Maan Gibraltar väestömäärä on 33691
```
Mikä on väestömäärältään Euroopan suurin maa?

### H6 Metsäpinta-ala
*AKTIVITEETTI: katsotaan Google Mapsista Suomen (Lahden) ja Irlannin satelliittikuvia. Katsotaan datasta metsäpinta-aloja. Minkälainen on Irlannin metsien historia?*  

Tee ohjelma, joka kysyy käyttäjältä maan nimeä, ja näyttää sitten kuinka suuri osa (%) kyseisen maan pinta-alasta on metsää. Data euroopan maiden metsäpinta-aloista on tiedostossa /data/maatiedot.json. 

Ohjelman esimerkkituloste:
```
Mikä maa? Ruotsi
Maan Ruotsi metsäpinta-ala on 68.6946060739977 % maapinta-alasta.
```

### H7 Suurin metsäpinta-ala
*Esimerkki: E7_pisin_oppilas*  

Tee ohjelma, joka etsii sen Euroopan maan, jonka maa-alasta on kaikkein suurin osuus metsää. Ohjelman tulee sitten näyttää maan nimi ja tieto siitä, kuinka suuri osa (%) kyseisen maan pinta-alasta on metsää. Data euroopan maiden metsäpinta-aloista on tiedostossa /data/maatiedot.json. 

Ohjelman esimerkkituloste:
```
Suhteessa eniten metsäpinta-alaa on maassa Mikämikämaa (50.0000000000 %)
```
Ota mallia esimerkkiohjelmasta, jossa etsitään pisin oppilas.

### H8 Lipun tunnistaminen
Uudet aiheet:  
- Satunnaisuus (random)
- Kuvan näyttäminen

Tehtäväpohjassa on koodia, joka hakee yhden maan lipun internetistä (json-tiedosdossa määritellystä osoitteesta) ja näyttää sen käyttäjälle. Täydennä annettua koodia, ja tee peli, jossa pelaajalle näytetään jonkun satunnaisen Euroopan maan lippu. Pelaajan pitää tunnistaa lippu ja nimetä maa. Jos vastaus on oikein, peli tulostaa "Hienoa, oikein!". Jos vastaus on väärin, näytä viesti, joka kertoo oikean vastauksen. Esimerkiksi "Ou nou, väärin! Oikea vastaus oli Ruotsi."

HUOM: jotta saat tehtäväpohjan toimimaan, aja ensin Visual Studio Coden terminaalissa seuraavat kaksi komentoa, jotka asentavat pythonin työkaluja tietojen hakemista ja kuvan näyttämistä varten: 
```
pip install requests
pip install Pillow
```

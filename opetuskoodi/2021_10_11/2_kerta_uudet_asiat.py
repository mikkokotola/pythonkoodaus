# Uusia asioita, kerta 2

# Muuttujat
nimi = input("Anna nimesi: ")
print("Moi vaan, " + nimi)
nimi = "Lasse"
print("Terve, " + nimi)
nimi = "Tarja"
print("Morjesta, " + nimi)

# Muuttujan käyttö useita kertoja
lempiruoka = input("Mikä on lempiruokasi? ")
print("Lempiruokasi on " + lempiruoka)
print("Tässä lisää: " + lempiruoka + lempiruoka + lempiruoka)

# Useita muuttujia
etunimi = "Pekka"
sukunimi = "Pythonen"

nimi = etunimi + " " + sukunimi
print(nimi)

# Numero muuttujassa
luku1 = 100
luku2 = "100"

print(luku1 + luku1)
print(luku2 + luku2)

kengännumero = 47
print("Sinun kengännumerosi on " + kengännumero) # Virhe - ei voi yhdistää merkkijonoa ja numeroa
print("Sinun kengännumerosi on " + int(kengännumero))

# F-merkkijono
tulos = 10 * 5
print(f"Tulos on {tulos}")

# Liukuluvut = desimaaliluvut

luku1 = 3.5
luku2 = 1.25

tulos = luku1 - luku2
print(f"Tulos on {tulos}")
print(f"{luku1} - {luku2} = {tulos}")

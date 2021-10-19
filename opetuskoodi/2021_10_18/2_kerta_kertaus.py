# Kertaus, kerta 3

# Muuttujat ja syötteen lukeminen käyttäjältä
nimi = input("Anna nimesi: ")
kengännumero = input("Mikä on kengännumerosi: ")
print("Moi vaan, " + nimi + "! Kengännumerosi on " + kengännumero + ".")

# F-merkkijono
print(f"Moi vaan, {nimi}! Kengännumerosi on {kengännumero}.")


# Numerot
# Ikälaskuri
syntymävuosi = input("Mikä on syntymävuotesi? ") 
syntymävuosi = int(syntymävuosi) # Muunnetaan merkkijono kokonaisluvuksi, jotta voimme laskea sillä
ikä = 2021 - syntymävuosi
print(f"Ikäsi vuoden 2021 lopussa on {ikä}")



# Laskin, joka osaa kertoa lukuja
luku1 = int(input("Anna luku: "))
luku2 = int(input("Anna toinen luku: "))
tulos = luku1 * luku2
print(f"{luku1} * {luku2} = {tulos}") 

# Laskin, joka laskee kolmen luvun summan
summa = 0
luku = int(input("Ensimmäinen luku: "))
summa = summa + luku

luku = int(input("Toinen luku: "))
summa = summa + luku

luku = int(input("kolmas luku: "))
summa = summa + luku

print(f"Lukujen summa: {summa}")

# Minkälaisia laskuja voi laskea
print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5//2)
print(5%2)

print(2 + 2 * 3)
print((2 + 2) * 3)

# Liukuluvut = desimaaliluvut
luku1 = 4.0
luku2 = 1.5

tulos = luku1 - luku2
print(f"Tulos on {tulos}")
print(f"{luku1} - {luku2} = {tulos}")

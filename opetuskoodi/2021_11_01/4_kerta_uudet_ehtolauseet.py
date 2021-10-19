# Ehtolauseet, kerta 3

# Esim. 1: yhtäsuuruus
ikä = int(input("Minkä ikäinen olet?"))
if ikä == 11:
    print("Olet vitosella tai kutosella")
print("Kiitos ja moi!")

# Esim. 2: pienempi kuin
ikä = int(input("Minkä ikäinen olet?"))
if ikä < 7:
    print("Taidat olla vielä päiväkodissa")
print("Kiitos ja moi!")

# Esim. 3: kulman luokittelu
kulman_suuruus = int(input("Anna kulman suuruus asteina: "))

if kulman_suuruus < 90:
    print("Kyseessä on terävä kulma.")

if kulman_suuruus == 90:
    print("Kyseessä on suora kulma.")

if kulman_suuruus > 90:
    print("Kyseessä on tylppä kulma.")

print("Kiitos ja moi!")

# Esim. 4: onko merkkijono sama
salasana = input("Anna salasana: ")

if salasana == "kissa":
    print("Tiesit salasanan!")
    print("Olet siis joko oikea käyttäjä...")
    print("...tai melkoinen hakkerivelho.")

print("Ohjelman suoritus päättyi. Kiitos ja hei!")

# Vertailuoperaattorit
# Yhtä suuri
print(5 == 5) 
print("kissa" == "kissa")

# Eri suuri
print(5 != 4) 
print("kisa" != "kissa")
print("Kissa" != "kissa")

# Suurempi
print(5 > 4)

# Suurempi tai yhtä suuri
print(5 >= 4)
print(5 >= 5)

# Pienempi
print(7 < 8)

# Pienempi tai yhtä suuri
print(7 <= 8)
print(7 <= 7)

# Mitä tarkoittaa?
print("Aatami" < "Bertta")
print("A" < "B")


# Visa
print(6 == 5)
print(7 < 9)
print("Olli" < "Pertti")
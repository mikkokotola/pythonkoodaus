# Ehtolauseet, kerta 3

# Esim. 1: yhtäsuuruus
ikä = int(input("Minkä ikäinen olet?"))
if ikä == 11:
    print("Olet vitosella tai kutosella")

# Esim. 2: pienempi kuin
ikä = int(input("Minkä ikäinen olet?"))
if ikä < 7:
    print("Taidat olla vielä päiväkodissa")


# Esim. 3: luvun luokittelu
luku = int(input("Anna luku: "))

if luku < 0:
    print("Luku on negatiivinen.")

if luku > 0:
    print("Luku on positiivinen.")

if luku == 0:
    print("Luku on nolla.")


# Esim. 4: onko merkkijono sama
salasana = input("Anna salasana: ")

if salasana == "kissa":
    print("Tiesit salasanan!")
    print("Olet siis joko oikea käyttäjä...")
    print("...tai melkoinen hakkerivelho.")

print("Ohjelman suoritus päättyi. Kiitos ja hei!")

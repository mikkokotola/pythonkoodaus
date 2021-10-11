# Otetaan käyttöön pythonin moduuli time, joka tarjoaa työkaluja ajan käsittelyyn
import time

alku = time.perf_counter_ns()
for i in range(1):
    print(5 + 16)
    print(21 - 3)
    print(33 + 19)
    print(55 - 4)
    print(60 + 20)
loppu = time.perf_counter_ns()
kesto = (loppu - alku) / 1000000000 # Muunnetaan nanosekunneista sekunneiksi
print("Koodin ajo kesti " + str(kesto) + " sekuntia")

# kertaa_nopeampi = 15 / kesto
#print("Tietokone oli " + str(kertaa_nopeampi))
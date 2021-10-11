# Otetaan käyttöön pythonin moduuli time, joka tarjoaa työkaluja ajan käsittelyyn
import time

laskuri = 0

alku = time.perf_counter_ns()

for i in range(1000000):
    laskuri = laskuri + 1
    
print(str(laskuri))

loppu = time.perf_counter_ns()
kesto = (loppu - alku) / 1000000000 # Muunnetaan nanosekunneista sekunneiksi 
print("Koodin ajo kesti " + str(kesto) + " sekuntia")


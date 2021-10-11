import time

nollakohta = time.gmtime(0)
#print("Tietokoneen ajanlaskennan alkuaika: " + str(nollakohta))
nollakohta_muotoiltu = time.strftime("%a, %d.%m.%Y %H:%M:%S", nollakohta)
print("Tietokoneen ajanlaskennan alkuaika muotoiltuna: " + str(nollakohta_muotoiltu))

aika_nyt = time.gmtime()
#print("Aika nyt aikavyöhykkeellä 0 (Greenwichilla): " + str(aika_nyt))

aika_nyt_suomi = time.localtime()
print("Aika nyt Suomessa: " + str(aika_nyt_suomi))

aika_nyt_suomi_muotoiltu = time.strftime("%a, %d.%m.%Y %H:%M:%S", aika_nyt_suomi)
print("Aika nyt Suomessa: " + str(aika_nyt_suomi_muotoiltu))

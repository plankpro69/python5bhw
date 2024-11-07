import random

def ziehung_lotto():
    zahlen_menge = list(range(1, 46))
    gezogene_zahlen = random.sample(zahlen_menge, 6)
    gezogene_zahlen.sort()
    return gezogene_zahlen

def statistik_lotto(anzahl_ziehungen):
    haeufigkeits_statistik = {zahl: 0 for zahl in range(1, 46)}
    
    for _ in range(anzahl_ziehungen):
        gezogene_zahlen = ziehung_lotto()
        
        for zahl in gezogene_zahlen:
            haeufigkeits_statistik[zahl] += 1
    
    return haeufigkeits_statistik

anzahl_ziehungen = 1000
statistik = statistik_lotto(anzahl_ziehungen)

for zahl, haeufigkeit in statistik.items():
    print(f"Zahl {zahl} wurde {haeufigkeit} mal gezogen.")
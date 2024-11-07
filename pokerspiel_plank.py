import random

karten_pro_farbe = 13
karten_satz = 52

def get_farbe(karten_nummer):
    return karten_nummer // karten_pro_farbe

def get_wert(karten_nummer):
    return karten_nummer % karten_pro_farbe

def hohe_karte(karten):
    return "true"

def ein_paar(karten):
    for karte1 in karten:
        for karte2 in karten:
            if karte1 != karte2 and get_wert(karte1) == get_wert(karte2):
                return "true"
    return "false"

def zwei_paare(karten):
    werte_count = {}
    paare = 0
    for karte in karten:
        wert = get_wert(karte)
        werte_count[wert] = werte_count.get(wert, 0) + 1
    for count in werte_count.values():
        if count == 2:
            paare += 1
    return "true" if paare == 2 else "false"

def drilling(karten):
    werte_count = {}
    for karte in karten:
        wert = get_wert(karte)
        werte_count[wert] = werte_count.get(wert, 0) + 1
    return "true" if 3 in werte_count.values() else "false"

def strasse(karten):
    werte = sorted(get_wert(karte) for karte in karten)
    for i in range(1, len(werte)):
        if werte[i] - werte[i - 1] != 1:
            return "false"
    return "true"

def farbe(karten):
    erste_farbe = get_farbe(karten[0])
    for karte in karten[1:]:
        if get_farbe(karte) != erste_farbe:
            return "false"
    return "true"

def full_house(karten):
    werte_count = {}
    hat_drilling = hat_paar = False
    for karte in karten:
        wert = get_wert(karte)
        werte_count[wert] = werte_count.get(wert, 0) + 1
    for count in werte_count.values():
        if count == 3:
            hat_drilling = True
        elif count == 2:
            hat_paar = True
    return "true" if hat_drilling and hat_paar else "false"

def vierling(karten):
    werte_count = {}
    for karte in karten:
        wert = get_wert(karte)
        werte_count[wert] = werte_count.get(wert, 0) + 1
    return "true" if 4 in werte_count.values() else "false"

def strasse_farbe(karten):
    return "true" if strasse(karten) == "true" and farbe(karten) == "true" else "false"

def royal_flush(karten):
    return "true" if strasse_farbe(karten) == "true" and get_wert(karten[0]) == 8 else "false"

def ziehe_karten(anzahl):
    gezogene_karten = []
    while len(gezogene_karten) < anzahl:
        karte = random.randint(0, karten_satz - 1)
        if karte not in gezogene_karten:
            gezogene_karten.append(karte)
    return gezogene_karten

def kombination_bestimmen(karten):
    if royal_flush(karten) == "true":
        return "Royal Flush"
    if strasse_farbe(karten) == "true":
        return "Straight Flush"
    if vierling(karten) == "true":
        return "Four of a Kind"
    if full_house(karten) == "true":
        return "Full House"
    if farbe(karten) == "true":
        return "Flush"
    if strasse(karten) == "true":
        return "Straight"
    if drilling(karten) == "true":
        return "Three of a Kind"
    if zwei_paare(karten) == "true":
        return "Two Pair"
    if ein_paar(karten) == "true":
        return "One Pair"
    return "High Card"

def statistik(anzahl_spiele):
    kombinationen = {
        "High Card": 0,
        "One Pair": 0,
        "Two Pair": 0,
        "Three of a Kind": 0,
        "Straight": 0,
        "Flush": 0,
        "Full House": 0,
        "Four of a Kind": 0,
        "Straight Flush": 0,
        "Royal Flush": 0
    }
    for _ in range(anzahl_spiele):
        karten = ziehe_karten(5)
        kombination = kombination_bestimmen(karten)
        kombinationen[kombination] += 1
    
    print("Prozentuale Verteilung:")
    for kombination in kombinationen:
        kombinationen[kombination] = kombinationen[kombination] / anzahl_spiele * 100
    return kombinationen

def statistik_anzeigen(anzahl_spiele):
    ergebnisse = statistik(anzahl_spiele)
    print(f"Statistik für {anzahl_spiele} Spiele:")
    for kombination, anteil in ergebnisse.items():
        print(f"{kombination}: {anteil:.5f}%")

statistik_anzeigen(10000)

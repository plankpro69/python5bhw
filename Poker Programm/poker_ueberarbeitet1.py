import random

def get_farbe(karten_nummer, karten_pro_farbe):
    return karten_nummer // karten_pro_farbe

def get_wert(karten_nummer, karten_pro_farbe):
    return karten_nummer % karten_pro_farbe

def hohe_karte():
    return True

def ein_paar(karten, karten_pro_farbe):
    for karte1 in karten:
        for karte2 in karten:
            if karte1 != karte2 and get_wert(karte1, karten_pro_farbe) == get_wert(karte2, karten_pro_farbe):
                return True
    return False

def zwei_paare(karten, karten_pro_farbe):
    werte_count = {}
    paare = 0
    for karte in karten:
        wert = get_wert(karte, karten_pro_farbe)
        werte_count[wert] = werte_count.get(wert, 0) + 1
    for count in werte_count.values():
        if count == 2:
            paare += 1
    return paare == 2

def drilling(karten, karten_pro_farbe):
    werte_count = {}
    for karte in karten:
        wert = get_wert(karte, karten_pro_farbe)
        werte_count[wert] = werte_count.get(wert, 0) + 1
    return 3 in werte_count.values()

def strasse(karten, karten_pro_farbe):
    werte = sorted(get_wert(karte, karten_pro_farbe) for karte in karten)
    for i in range(1, len(werte)):
        if werte[i] - werte[i - 1] != 1:
            return False
    return True

def farbe(karten, karten_pro_farbe):
    erste_farbe = get_farbe(karten[0], karten_pro_farbe)
    for karte in karten[1:]:
        if get_farbe(karte, karten_pro_farbe) != erste_farbe:
            return False
    return True

def full_house(karten, karten_pro_farbe):
    werte_count = {}
    hat_drilling = hat_paar = False
    for karte in karten:
        wert = get_wert(karte, karten_pro_farbe)
        werte_count[wert] = werte_count.get(wert, 0) + 1
    for count in werte_count.values():
        if count == 3:
            hat_drilling = True
        elif count == 2:
            hat_paar = True
    return hat_drilling and hat_paar

def vierling(karten, karten_pro_farbe):
    werte_count = {}
    for karte in karten:
        wert = get_wert(karte, karten_pro_farbe)
        werte_count[wert] = werte_count.get(wert, 0) + 1
    return 4 in werte_count.values()

def strasse_farbe(karten, karten_pro_farbe):
    return strasse(karten, karten_pro_farbe) and farbe(karten, karten_pro_farbe)

def royal_flush(karten, karten_pro_farbe):
    return strasse_farbe(karten, karten_pro_farbe) and get_wert(karten[0], karten_pro_farbe) == 8

def ziehe_karten(anzahl, karten_satz):
    gezogene_karten = []
    while len(gezogene_karten) < anzahl:
        karte = random.randint(0, karten_satz - 1)
        if karte not in gezogene_karten:
            gezogene_karten.append(karte)
    return gezogene_karten

def kombination_bestimmen(karten, karten_pro_farbe):
    if royal_flush(karten, karten_pro_farbe):
        return "Royal Flush"
    if strasse_farbe(karten, karten_pro_farbe):
        return "Straight Flush"
    if vierling(karten, karten_pro_farbe):
        return "Four of a Kind"
    if full_house(karten, karten_pro_farbe):
        return "Full House"
    if farbe(karten, karten_pro_farbe):
        return "Flush"
    if strasse(karten, karten_pro_farbe):
        return "Straight"
    if drilling(karten, karten_pro_farbe):
        return "Three of a Kind"
    if zwei_paare(karten, karten_pro_farbe):
        return "Two Pair"
    if ein_paar(karten, karten_pro_farbe):
        return "One Pair"
    return "High Card"

def statistik(anzahl_spiele, karten_satz, karten_pro_farbe):
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
        karten = ziehe_karten(5, karten_satz)
        kombination = kombination_bestimmen(karten, karten_pro_farbe)
        kombinationen[kombination] += 1
    
    for kombination in kombinationen:
        kombinationen[kombination] = kombinationen[kombination] / anzahl_spiele * 100
    return kombinationen

def statistik_anzeigen(anzahl_spiele, karten_satz, karten_pro_farbe):
    ergebnisse = statistik(anzahl_spiele, karten_satz, karten_pro_farbe)
    print(f"Statistik für {anzahl_spiele} Spiele:")
    for kombination, anteil in ergebnisse.items():
        print(f"{kombination}: {anteil:.2f}%")

def main():
    karten_pro_farbe = 13
    karten_satz = 52

    try:
        anzahl_spiele = int(input("Gib die Anzahl der Spiele ein: "))
        if anzahl_spiele <= 0:
            raise ValueError("Die Anzahl der Spiele muss positiv sein.")
    except ValueError as e:
        print(f"Ungültige Eingabe: {e}")
        return

    print("\nSimulation läuft...")
    statistik_anzeigen(anzahl_spiele, karten_satz, karten_pro_farbe)
    print("\nSimulation abgeschlossen.")

if __name__ == "__main__":
    main()
import random
import functools
import time

class PokerSpiel:
    KARTEN_PRO_FARBE = 13
    KARTEN_SATZ = 52

    def __init__(self, anzahl_spiele=10000):
        self.anzahl_spiele = anzahl_spiele

    @staticmethod
    def timer(func):
        """Print the runtime of the decorated function"""
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):
            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"Finished {func.__name__}() in {run_time:.4f} secs")
            return value
        return wrapper_timer

    def get_farbe(self, karten_nummer):
        return karten_nummer // self.KARTEN_PRO_FARBE

    def get_wert(self, karten_nummer):
        return karten_nummer % self.KARTEN_PRO_FARBE

    def ein_paar(self, karten):
        werte = [self.get_wert(k) for k in karten]
        return "true" if len(set(werte)) < len(werte) else "false"

    def zwei_paare(self, karten):
        werte_count = {}
        for karte in karten:
            wert = self.get_wert(karte)
            werte_count[wert] = werte_count.get(wert, 0) + 1
        return "true" if list(werte_count.values()).count(2) == 2 else "false"

    def drilling(self, karten):
        werte_count = {}
        for karte in karten:
            wert = self.get_wert(karte)
            werte_count[wert] = werte_count.get(wert, 0) + 1
        return "true" if 3 in werte_count.values() else "false"

    def strasse(self, karten):
        werte = sorted(self.get_wert(karte) for karte in karten)
        return "true" if all(werte[i] - werte[i - 1] == 1 for i in range(1, len(werte))) else "false"

    def farbe(self, karten):
        return "true" if len(set(self.get_farbe(k) for k in karten)) == 1 else "false"

    def full_house(self, karten):
        werte_count = [self.get_wert(k) for k in karten]
        return "true" if sorted(werte_count.count(v) for v in set(werte_count)) == [2, 3] else "false"

    def vierling(self, karten):
        werte_count = [self.get_wert(k) for k in karten]
        return "true" if 4 in [werte_count.count(v) for v in set(werte_count)] else "false"

    def strasse_farbe(self, karten):
        return "true" if self.strasse(karten) == "true" and self.farbe(karten) == "true" else "false"

    def royal_flush(self, karten):
        return "true" if self.strasse_farbe(karten) == "true" and self.get_wert(karten[0]) == 8 else "false"

    def ziehe_karten(self, anzahl):
        return random.sample(range(self.KARTEN_SATZ), anzahl)

    def kombination_bestimmen(self, karten):
        if self.royal_flush(karten) == "true": return "Royal Flush"
        if self.strasse_farbe(karten) == "true": return "Straight Flush"
        if self.vierling(karten) == "true": return "Four of a Kind"
        if self.full_house(karten) == "true": return "Full House"
        if self.farbe(karten) == "true": return "Flush"
        if self.strasse(karten) == "true": return "Straight"
        if self.drilling(karten) == "true": return "Three of a Kind"
        if self.zwei_paare(karten) == "true": return "Two Pair"
        if self.ein_paar(karten) == "true": return "One Pair"
        return "High Card"

    @timer
    def statistik(self):
        kombinationen = {k: 0 for k in [
            "High Card", "One Pair", "Two Pair", "Three of a Kind", "Straight", "Flush",
            "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]}
        
        for _ in range(self.anzahl_spiele):
            karten = self.ziehe_karten(5)
            kombination = self.kombination_bestimmen(karten)
            kombinationen[kombination] += 1

        for kombination in kombinationen:
            kombinationen[kombination] = kombinationen[kombination] / self.anzahl_spiele * 100
        return kombinationen

    def statistik_anzeigen(self):
        ergebnisse = self.statistik()
        print(f"Statistik für {self.anzahl_spiele} Spiele:")
        for kombination, anteil in ergebnisse.items():
            print(f"{kombination}: {anteil:.5f}%")

if __name__ == "__main__":
    spiel = PokerSpiel(anzahl_spiele=10000)
    spiel.statistik_anzeigen()

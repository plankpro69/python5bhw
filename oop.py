class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Mitarbeiter(Person):
    def __init__(self, name, gender, abteilung):
        super().__init__(name, gender)
        self.abteilung = abteilung


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, gender, abteilung):
        super().__init__(name, gender, abteilung)


class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []
        self.leiter = None

    def set_leiter(self, leiter):
        if not isinstance(leiter, Abteilungsleiter):
            raise ValueError("Der Leiter muss ein Abteilungsleiter sein.")
        self.leiter = leiter
        self.add_mitarbeiter(leiter)

    def add_mitarbeiter(self, mitarbeiter):
        if not isinstance(mitarbeiter, Mitarbeiter):
            raise ValueError("Nur Mitarbeiter können hinzugefügt werden.")
        self.mitarbeiter.append(mitarbeiter)

    def mitarbeiter_count(self):
        return len(self.mitarbeiter)


class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def add_abteilung(self, abteilung):
        if not isinstance(abteilung, Abteilung):
            raise ValueError("Nur Abteilungen können hinzugefügt werden.")
        self.abteilungen.append(abteilung)

    def mitarbeiter_count(self):
        return sum(abteilung.mitarbeiter_count() for abteilung in self.abteilungen)

    def abteilungsleiter_count(self):
        return sum(1 for abteilung in self.abteilungen if abteilung.leiter is not None)

    def abteilungs_count(self):
        return len(self.abteilungen)

    def groesste_abteilung(self):
        return max(self.abteilungen, key=lambda abt: abt.mitarbeiter_count(), default=None)

    def gender_verteilung(self):
        frauen = sum(1 for abteilung in self.abteilungen for mitarbeiter in abteilung.mitarbeiter if mitarbeiter.gender == "weiblich")
        maenner = sum(1 for abteilung in self.abteilungen for mitarbeiter in abteilung.mitarbeiter if mitarbeiter.gender == "männlich")
        gesamt = frauen + maenner
        if gesamt == 0:
            return {"weiblich": 0, "männlich": 0}
        return {
            "weiblich": (frauen / gesamt) * 100,
            "männlich": (maenner / gesamt) * 100,
        }


# Beispiel-Daten:
firma = Firma("Beispiel GmbH")

abteilung1 = Abteilung("IT")
abteilung2 = Abteilung("HR")

leiter1 = Abteilungsleiter("Max Mustermann", "männlich", abteilung1)
abteilung1.set_leiter(leiter1)

mitarbeiter1 = Mitarbeiter("Anna Müller", "weiblich", abteilung1)
abteilung1.add_mitarbeiter(mitarbeiter1)

mitarbeiter2 = Mitarbeiter("Hans Meier", "männlich", abteilung2)
abteilung2.add_mitarbeiter(mitarbeiter2)

leiter2 = Abteilungsleiter("Lisa Schmidt", "weiblich", abteilung2)
abteilung2.set_leiter(leiter2)

firma.add_abteilung(abteilung1)
firma.add_abteilung(abteilung2)

# Methoden testen:
print(f"Mitarbeiter insgesamt: {firma.mitarbeiter_count()}")
print(f"Abteilungsleiter insgesamt: {firma.abteilungsleiter_count()}")
print(f"Anzahl der Abteilungen: {firma.abteilungs_count()}")
print(f"Größte Abteilung: {firma.groesste_abteilung().name}")
print(f"Geschlechterverteilung: {firma.gender_verteilung()}")

class Mitarbeiter:
    def __init__(self, name, gehalt):
        self.name = name
        self.gehalt = gehalt

    def info(self):
        return f"{self.name} verdient {self.gehalt} €."


class Manager(Mitarbeiter):
    def __init__(self, name, gehalt, bonus):
        super().__init__(name, gehalt) 
        self.bonus = bonus

    def infomanager(self):
        grundlage = super().info() 
        return f"{grundlage} Zusätzlich erhält er/sie einen Bonus von {self.bonus} €."


mitarbeiter = Mitarbeiter("Anna", 3000)
print(mitarbeiter.info())

manager = Manager("Tom", 5000, 2000)
print(manager.infomanager())

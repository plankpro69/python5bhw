import sys

class Mitarbeiter:
    def __init__(self, name, gehalt):
        # Fehlerbehandlung: neuer Fehler und behebar (A)
        self.name = name
        self.gehalt = gehalt
        if gehalt == 0:
            gehalt = "unknown"

    def get_name(self):
        return self.name
    def get_gehalt(self):
        return self.gehalt
    def set_name(self, name):
        self.name = name
    def set_gehalt(self, gehalt):
        if gehalt < 0:                # Fehler C (neu und nicht behebar)
            raise ValueError('Gehalt muss mehr sein')    # wirf Fehler weiter
        self.gehalt = gehalt

    def get_infos(self):
        try:
            return self.get_name(), self.get_gehalt()  # Fehler B (hochblubber und behebar)
        except AttributeError:
            return self.set_name('Unknow'), self.set_gehalt('Unknown')    # setzte Unknown
        
    def __str__(self):
            return f'{self.name}, {self.gehalt}'
    

class Manager(Mitarbeiter):
    def __init__(self, name, gehalt, bonus):
        super().__init__(name, gehalt)    
        self.bonus = bonus

    def infomanager(self):
        return f"{self.name} erhält einen Bonus von {self.bonus} €."
    
    def __str__(self):
            return f'{self.name}, {self.gehalt}'


def main():
    a1 = Mitarbeiter('Hans', 3000)
    a2 = Mitarbeiter('Johannes', 2000)
    m1 = Manager('Hannes', 7000, 300)
    print(a1)
    print(a1.get_infos())
    print(a2)
    print(m1)

if __name__ == '__main__':
    try:
        main()
    except Exception as error:    # Fehler D (hochblubber und nicht behebar), wenn
        print(f'Error: {error}')    # Fehler auftritt, mach nicht weiter
        sys.exit(1)
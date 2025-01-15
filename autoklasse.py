class Auto:
    def __init__(self, ps):
        if not isinstance(ps, (int, float)) or ps < 0:
            raise ValueError("PS muss eine positive Zahl sein.")
        self.ps = ps

    def __add__(self, other):
        if isinstance(other, Auto):
            return self.ps + other.ps
        raise TypeError("Addition ist nur mit anderen Auto-Objekten möglich.")

    def __sub__(self, other):
        if isinstance(other, Auto):
            return self.ps - other.ps
        raise TypeError("Subtraktion ist nur mit anderen Auto-Objekten möglich.")

    def __mul__(self, other):
        if isinstance(other, Auto):
            return self.ps * other.ps
        raise TypeError("Multiplikation ist nur mit anderen Auto-Objekten möglich.")

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        return False

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        raise TypeError("Vergleich ist nur mit anderen Auto-Objekten möglich.")

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        raise TypeError("Vergleich ist nur mit anderen Auto-Objekten möglich.")

    def __len__(self):
        return int(self.ps)

if __name__ == "__main__":
    a1 = Auto(50)
    a2 = Auto(60)

    print(f"Addition: {a1 + a2}") 

    print(f"Subtraktion: {a2 - a1}")

    print(f"Multiplikation: {a1 * a2}") 

    print(f"EQ: {a1 == a2}") 

    print(f"LT: {a1 < a2}") 

    print(f"GT: {a2 > a1}") 

    print(f"Länge von a1: {len(a1)}") 

    try:
        print(a1 + 10)  # TypeError
    except TypeError as e:
        print(e)

    try:
        print(a1 < 10)  #auch TypeError
    except TypeError as e:
        print(e)
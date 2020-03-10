class Calculator():
    def __init__(self):
        self.ostatnia_liczba = 0

    def dodaj(self, x, y):
        wynik = x + y
        self.ostatnia_liczba = wynik
        print(wynik)

    def odejmij(self, x, y):
        wynik = x - y
        self.ostatnia_liczba = wynik
        print(wynik)

    def mnożenie(self, x, y):
        wynik = x * y
        self.ostatnia_liczba = wynik
        print(wynik)

    def dzielenie(self, x, y):
        wynik = x / y
        self.ostatnia_liczba = wynik
        print(wynik)


calc = Calculator()
calc.dodaj(3,5)
calc.mnożenie(3,7)
calc.dzielenie(100, 25)

calc2 = Calculator()
calc2.odejmij(2, 16)
print("ostatnia liczba to calc: {}".format(calc.ostatnia_liczba))
print("ostatnia liczba to calc2: {}".format(calc2.ostatnia_liczba))




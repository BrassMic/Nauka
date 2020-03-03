def dodaj(x, y):
    return x + y


def odejmij(x, y):
    return x - y


def mnożenie(x, y):
    return x * y


def dzielenie(x, y):
    return x / y


print("Wybierz funkcję:")
print('1.Dodawanie')
print('2.Odejmownie')
print('3.Mnożenie')
print('4.dzielenie')
choice = input("Wybierz opcję (1,2,3,4):")
num1 = float(input("Liczba 1:"))
num2 = float(input("Liczba 2:"))
if choice == "1":
    print(num1, "+", num2, "=", dodaj(num1, num2))
elif choice == "2":
    print(num1, "-", num2, "=", odejmij(num1, num2))
elif choice == "3":
    print(num1, "*", num2, "=", mnożenie(num1, num2))
elif choice == "4":
    print(num1, ":", num2, "=", dzielenie(num1, num2))
else:
    print("Niepoprawna wartość")

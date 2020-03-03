# do przerobienia kod z kalkulatora
def Euro(x, y):
    return x * y


def Dulary(x, z):
    return x * z
y = 4.26
z = 3.88


print("Waluty:")
print('1.Euro')
print('2.Dulary')

choice = input("Wybierz walutę (1/2):")
num1 = float(input("Kwota:"))

if choice == "1":
    print(num1, "*", y, "=", Euro(num1, y))
elif choice == "2":
    print(num1, "*", y, "=", Dulary(num1, z))

else:
    print("Niepoprawna wartość")
# łaaat? siadło za pierwszym razem
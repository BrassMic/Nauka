x = input("Podaj swoje imię:")
print("Podane przez Ciebie imię to:", x)
y = (input("Czy podałeś właściwe dane? Wpisz Tak/Nie:"))
if y == "tak":
    print("Dziękuję za szczerość")
elif y == "nie":
    print("Mały oszust")
else:
    print("Nie pogrywaj z tym botem")
z = input("Podaj nazwisko:")
print("Twoje nazwisko to:", z)
print("Reasumując, nazywasz się:", x,  z)

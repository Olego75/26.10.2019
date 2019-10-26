x = 5
krotka = ("element", "drugi_element")

ciag_znakow = "Nasza liczba to {} balala baalbs {}, {}"

print(f"Nasza liczba to {x + 10} bala balbs {krotka}")
print("Nasza liczba to {} bala balbs {}, {}".format(x + 15, krotka, {2: "sd"}))
print('Nasza liczba to', x)

Name = input("Wprowadz imie:")
Nazwisko = input("Wprowadz nazwisko:")

print("Twoje Imie", Name, "Twoje Nazwisko", Nazwisko)
print(f"Twoje Imie {Name.capitalize()} Twoje Nazwisko {Nazwisko.capitalize()}")
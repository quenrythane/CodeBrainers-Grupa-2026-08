
imie = input("podaj imie: ")
try:
    wiek = int(input("podaj wiek: "))
except:
    wiek = "Nie podano liczby"

print(f"Hello {imie}. Masz {wiek} lat")





imie = input("podaj imie: ")
try:  # if
    wiek = int(input("podaj wiek: "))
except:  # else
    wiek = "Nie podano liczby"

print(f"Hello {imie}. Masz {wiek} lat")



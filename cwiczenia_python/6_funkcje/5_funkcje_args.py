"""
def dodaj(*liczby):
    # liczby = (2, 4, 5)
    wynik = 0
    for liczba in liczby:
        wynik += liczba
    return wynik

wynik = dodaj(2, 4, 5, 6)
print(wynik)
"""

def hello(*imiona):
    for imie in imiona:
        print(f"Hello {imie}")


# hello("Ania", "Bartek", "Czarek", "Damian")


lista_imion = ["Ania", "Bartek", "Czarek"]
hello(lista_imion)  # tutaj jeden arguemnt - jedna lista
hello(*lista_imion)  # tutaj rozpakowujemy liste i przekazujemy kazdy element jako osobny argument


def zapisz_oceny_ucznia(imie, *oceny):
    """
    Dla podanego imienia i dowolnej liczby ocen
    Oblicz średnią i wypisz komunikat:
    "Uczeń Adam ma średnią: 4.5"
    """
    suma_ocen = 0
    for ocena in oceny:
        suma_ocen += ocena

    srednia = suma_ocen / len(oceny)
    print(f"Uczeń {imie} ma średnią: {srednia}")

zapisz_oceny_ucznia("Adam", 2, 3, 4, 5)

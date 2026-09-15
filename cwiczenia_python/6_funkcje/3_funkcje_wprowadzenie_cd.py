# w funkcji możemy podpowiadać jakie typy danych przyjmują dane arguemnty i jaki typ danych funkcja zwróci
def zrob_herbate(imie: str, rodzaj_herbaty: str = "czarna") -> str:
    """
    To jest docsstring czyli dokumentacja funkcji którą możemy przygotować
    Funkcja, która przygotowuje herbatę dla danej osoby
    """
    print(f"Przygotuj kubek {imie}")
    print(f"Przygotuj {rodzaj_herbaty} herbata")
    print("Nalać wody do czajnika")
    print("Zagotuj wodę")
    print("Włóż herbatę do kubka")
    print("Zalej kubek wrzątkiem")
    print("Odstaw na 3 minuty")
    print("Wyjmij torebke z kubka")
    print(f"Herbata dla {imie} jest gotowa!")
    print()
    return f"Herbata dla {imie} jest gotowa!"

# uruchamiając funkcje możemy doprecyzować dla jakiego parametru chcemy przypisać daną wartość
zrob_herbate(imie="Tomek")

"""
Prezentacja użycia *args w funkcjach Python.

*args (skrót od "arguments") pozwala na przekazywanie dowolnej liczby argumentów
pozycyjnych do funkcji. Wewnątrz funkcji argumenty te są dostępne jako KROTKA (tuple).
Gwiazdka (*) przed nazwą zmiennej odpowiada za pakowanie/rozpakowywanie argumentów.
"""

# 1. Podstawowy przykład - funkcja sumująca dowolną liczbę liczb
def zsumuj_liczby(*args: int | float) -> int | float:
    """Funkcja przyjmuje dowolną liczbę liczb i zwraca ich sumę."""
    print(f"Typ przekazanych *args: {type(args)}, zawartość: {args}")
    suma = 0
    for liczba in args:
        suma += liczba
    return suma


# 2. Łączenie zwykłych argumentów pozycyjnych z *args
def zorganizuj_impreze(organizator: str, *goscie: str) -> None:
    """
    organizator - pierwszy wymagany argument pozycyjny
    *goscie - dowolna liczba pozostałych gości
    """
    print(f"Organizator imprezy: {organizator}")
    if goscie:
        print("Lista zaproszonych gości:")
        for i, gosc in enumerate(goscie, start=1):
            print(f"  {i}. {gosc}")
    else:
        print("Brak dodatkowych gości.")
    print()


# 3. Przykład praktyczny (QA / Testowanie) - generowanie logów z wielu komunikatów
def zapisz_logi(poziom_logu: str, *komunikaty: str) -> None:
    """Zapisuje wpis w logu z nagłówkiem poziomu i dowolną liczbą wiadomości."""
    print(f"[{poziom_logu.upper()}] Zgłoszone zdarzenia:")
    for wpis in komunikaty:
        print(f"  - {wpis}")
    print("-" * 40)


# --- URUCHOMIENIE I PREZENTACJA ---

if __name__ == "__main__":
    print("=== 1. Podstawowy przykład sumowania ===")
    print("Suma (1, 2, 3):", zsumuj_liczby(1, 2, 3))
    print("Suma (10, 20, 30, 40, 50):", zsumuj_liczby(10, 20, 30, 40, 50))
    print("Suma bez argumentów:", zsumuj_liczby())
    print()

    print("=== 2. Łączenie argumentu stałego i *args ===")
    zorganizuj_impreze("Ania", "Bartek", "Czarek", "Damian")
    zorganizuj_impreze("Tomek")  # bez dodatkowych gości

    print("=== 3. Przykład praktyczny (Logowanie w testach QA) ===")
    zapisz_logi("INFO", "Inicjalizacja przeglądarki Chrome", "Otwarcie strony logowania")
    zapisz_logi("ERROR", "Element #submit-btn nie został znaleziony", "Timeout 5000ms", "Zrzut ekranu zapisany do error.png")

    print("=== 4. Rozpakowywanie listy/krotki za pomocą gwiazdki (*) ===")
    lista_liczb = [5, 10, 15, 20]
    # Przekazanie listy z gwiazdką rozpakowuje jej elementy jako osobne argumenty pozycyjne
    wynik = zsumuj_liczby(*lista_liczb)  # odpowiednik: zsumuj_liczby(5, 10, 15, 20)
    print("Suma rozpakowanej listy [5, 10, 15, 20]:", wynik)

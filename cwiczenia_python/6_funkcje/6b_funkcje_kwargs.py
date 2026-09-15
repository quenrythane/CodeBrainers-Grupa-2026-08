"""
Prezentacja użycia **kwargs w funkcjach Python oraz łączenia *args i **kwargs.

**kwargs (skrót od "keyword arguments") pozwala na przekazywanie dowolnej liczby
argumentów nazwanych (klucz=wartość). Wewnątrz funkcji są one dostępne jako SŁOWNIK (dict).
Dwie gwiazdki (**) odpowiadają za pakowanie/rozpakowywanie argumentów słownikowych.
"""

# 1. Podstawowy przykład - profil użytkownika z dowolnymi metadanymi
def wyswietl_profil(imie: str, nazwisko: str, **dodatkowe_dane: str | int | bool) -> None:
    """
    imie, nazwisko - wymagane argumenty pozycyjne
    **dodatkowe_dane - słownik zawierający dowolne argumenty nazwane
    """
    print(f"Profil: {imie} {nazwisko}")
    print(f"Typ **kwargs: {type(dodatkowe_dane)}, zawartość: {dodatkowe_dane}")

    if dodatkowe_dane:
        print("Dodatkowe informacje:")
        for klucz, wartosc in dodatkowe_dane.items():
            print(f"  - {klucz}: {wartosc}")
    else:
        print("Brak dodatkowych informacji.")
    print()


# 2. Łączenie wszystkich typów argumentów w odpowiedniej kolejności:
# Kolejność parametrów: 1. zwykłe pozycyjne, 2. *args, 3. zwykłe z wartością domyślną, 4. **kwargs
def uruchom_przypadek_testowy(id_testu: str, *tagi: str, srodowisko: str = "STAGING", **konfiguracja) -> None:
    """
    Kompleksowa funkcja demonstrująca łączenie *args i **kwargs w scenariuszach QA.
    """
    print(f"--- Uruchamianie testu: {id_testu} na środowisku [{srodowisko}] ---")

    if tagi:
        print(f"Tagi testu: {', '.join(tagi)}")

    if konfiguracja:
        print("Parametry konfiguracji testu:")
        for klucz, wartosc in konfiguracja.items():
            print(f"  * {klucz} = {wartosc}")
    print("-" * 50)


# --- URUCHOMIENIE I PREZENTACJA ---

if __name__ == "__main__":
    print("=== 1. Podstawowe użycie **kwargs ===")
    wyswietl_profil("Jan", "Kowalski", wiek=30, miasto="Warszawa", stanowisko="QA Engineer")
    wyswietl_profil("Anna", "Nowak")  # Bez argumentów słownikowych

    print("=== 2. Rozpakowywanie słownika za pomocą dwóch gwiazdek (**) ===")
    dane_z_bazy = {
        "wiek": 25,
        "email": "piotr@example.com",
        "aktywny": True
    }
    # Przekazanie słownika z ** rozpakowuje go jako argumenty nazwane (wiek=25, email=..., aktywny=...)
    wyswietl_profil("Piotr", "Zieliński", **dane_z_bazy)

    print("=== 3. Kompleksowe łączenie *args i **kwargs (Scenariusze QA) ===")
    # Przekazanie id_testu, 3 tagów (*args), zmiany środowiska domyślnego oraz parametrów konfiguracji (**kwargs)
    uruchom_przypadek_testowy(
        "TEST-101",
        "smoke", "regression", "critical",
        srodowisko="PRODUCTION",
        headless=True,
        timeout_sec=30,
        browser="chrome"
    )

    # Inne wywołanie ze środowiskiem domyślnym STAGING
    uruchom_przypadek_testowy(
        "TEST-102",
        "api",
        retry_count=3,
        validate_schema=True
    )

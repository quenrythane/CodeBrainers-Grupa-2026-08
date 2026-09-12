"""
stwórz slownik który będzie reprezentował Oceny uczniów.
Niech słownik będzie miał pięć imion, a do każdego imienia będzie dopisana dana ocena od 1 do 6.
Następnie zaktualizuj ocenę jednego z uczniów.

Jako weryfikacja zaimplementuj poniższe kroki:
- print słownik
- print wartość przed aktualizacją
- aktualizacja oceny
- print wartość po aktualizacji
"""

slowik_imiona_oceny = {
    "Anna": 5,
    "Jan": 4,
    "Katarzyna": 3,
    "Piotr": 2,
    "Michał": 1
}

print(slowik_imiona_oceny)
print(f'Ocena Michała przed zmianą: {slowik_imiona_oceny["Michał"]}')

slowik_imiona_oceny["Michał"] = 4
print(f'Ocena Michała po zmianie: {slowik_imiona_oceny["Michał"]}')

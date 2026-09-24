# stworzenie środowiska wirtualnego
# python -m venv .venv

# aktywacja środowiska wirtualnego
# .\.venv\Scripts\activate.bat

from kalkulator import *

def test_dodawanie():
    assert dodawanie(1, 5) == 6

def test_odejmowanie():
    assert odejmowanie(5, 1) == 6

def test_mnozenie():
    assert mnozenie(5, 1) == 5

def test_dzielenie():
    assert dzielenie(5, 1) == 5

def test_potegowanie():
    assert potegowanie(2, 3) == 8
    assert potegowanie(10, 2) == 100
    assert potegowanie(5, 3) == 125

# uruchamianie pojedynczego testu
# pytest testy_python\test_kalkulator.py::test_mnozenie

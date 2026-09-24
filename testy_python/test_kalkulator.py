# stworzenie środowiska wirtualnego
# python -m venv .venv

# aktywacja środowiska wirtualnego
# .\.venv\Scripts\activate.bat

from kalkulator import *

def test_dodawanie():
    assert dodawanie(1, 5) == 6

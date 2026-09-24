from kalkulator_2 import potegowanie
import pytest

@pytest.mark.wip
@pytest.mark.parametrize("podstawa, wykladnik, oczekiwany_wynik", [
    (2, 3, 8),
    (10, 2, 100),
    (5, 3, 125)
])
def test_potegowanie(podstawa, wykladnik, oczekiwany_wynik):
    assert potegowanie(podstawa, wykladnik) == oczekiwany_wynik

    # assert potegowanie(2, 3) == 8
    # assert potegowanie(10, 2) == 100
    # assert potegowanie(5, 3) == 125





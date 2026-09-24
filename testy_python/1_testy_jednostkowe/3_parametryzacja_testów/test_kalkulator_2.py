from kalkulator_2 import potegowanie
import pytest
import logging

logger = logging.getLogger(__name__)

@pytest.mark.wip
@pytest.mark.parametrize("podstawa, wykladnik, oczekiwany_wynik", [
    (2, 3, 8),
    (10, 2, 100),
    (5, 3, 125)
])
def test_potegowanie(podstawa, wykladnik, oczekiwany_wynik):
    logger.info(f"Testujemy potęgowanie: {podstawa} do potęgi {wykladnik}")
    assert potegowanie(podstawa, wykladnik) == oczekiwany_wynik

    # assert potegowanie(2, 3) == 8
    # assert potegowanie(10, 2) == 100
    # assert potegowanie(5, 3) == 125





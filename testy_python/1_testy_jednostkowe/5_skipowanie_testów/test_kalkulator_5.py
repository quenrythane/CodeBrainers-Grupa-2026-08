from kalkulator_2 import potegowanie
import pytest

@pytest.mark.xfail(reason="Niestabilne połaczenie z zewnetrznym dostawca")
def test_potegowanie_1():
    assert potegowanie(2, 3) == 10

@pytest.mark.skip(reason="Cos sie zepsulo i jeszcze to naprawiamy")
def test_potegowanie_2():
    assert potegowanie(2, 3) == 8

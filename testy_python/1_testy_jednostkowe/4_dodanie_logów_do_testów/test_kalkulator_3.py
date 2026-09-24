from kalkulator_2 import potegowanie
import pytest
import logging

logger = logging.getLogger(__name__)

@pytest.mark.logging
def test_potegowanie():
    logger.debug("Jestem debugiem")
    logger.info("Info Testujemy potegowanie")
    logger.warning("Jestem warningiem")
    logger.error("Jestem errorrm")
    logger.critical("Jestem criticalem")
    assert potegowanie(2, 3) == 8



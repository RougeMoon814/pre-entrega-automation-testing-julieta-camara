#Archivo conftest.py
import pytest

from utils.helpers import get_driver

#ejecutarlo en cada uno de los test.
@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

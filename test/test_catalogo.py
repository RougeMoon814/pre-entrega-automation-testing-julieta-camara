#testear que la url abra
from utils.helpers import login

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_catalogo_producto(driver):
    login(driver, "standard_user", "secret_sauce")

    #validar que haya productos en inventarios. Que contiene mis productos? -> clase inventory_item
    #productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    #conviene usar el data-test
    #el css selector me ayuda a encontrar atributos que no son clases o IDs.
    productos = driver.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item"]')
    #trae un html collection (normalmente vienen como una lista)
    #tenemos que saber si la lista tiene algo:
    assert len(productos) > 0

    nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre == "Sauce Labs Backpack"
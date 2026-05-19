#testear que la url abra
from utils.helpers import login

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(driver):
    #este driver sale de mi conf, tengo que pasarselo a la funcion.
    login(driver, "standard_user", "secret_sauce")
    #los correctos me da la pag

    #ahora si puedo hacer un assert (una ves iniciada sesion confirmar estar en la pag inventory)
    assert "inventory.html" in driver.current_url

    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"

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

def test_agregar_al_carrito(driver):
    login(driver, "standard_user", "secret_sauce")

    #verificar el nombre del producto
    nombre_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    wait = WebDriverWait(driver, 10)
    #si encuentra producto, que le de click para agregar producto
    btn_add = wait.until(
        #tengo que hacerlo a través de Xpath porque tengo mas de un elemento
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
    )

    btn_add.click()

    #validar contador
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"

    #entro en carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    #validar productos en carrito
    producto_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto_carrito == nombre_producto

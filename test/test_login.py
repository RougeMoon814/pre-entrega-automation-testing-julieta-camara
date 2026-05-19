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

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
#importo modulo para seleccionar dentro del dom (By)
from selenium.webdriver.common.by import By
#podemos poner esperas explicitas
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    service =Service(GeckoDriverManager().install())
    driver =webdriver.Firefox(service=service)
    #que esta funcion al ejecutar me devuelva el driver
    return driver

def login(driver, username, password):
    #funcion recibe el driver, comunica con el navegador

    #el implicity es global, no queremos
    #driver.implicityWait(10)

    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    username = wait.until(
    EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys(username)

    #seleccionar sin exception conditions
    driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.ID, "login-button").click()
    
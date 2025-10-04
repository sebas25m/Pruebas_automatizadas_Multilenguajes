from selenium import webdriver
from selenium.webdriver.common.by import By
from var import *
import time

counter = 1
def tomar_screenshot(driver, screen_name: str):
    global counter
    driver.save_screenshot(f"TC_pruebas_login/test_selenium/test_images/tc_03_{screen_name}_{counter}.png")
    counter += 1

driver = webdriver.Edge()
driver.get(link)
time.sleep(3)

tomar_screenshot(driver, "inicio_vacio")
time.sleep(1)

driver.find_element(By.XPATH, uname_input).send_keys("")
driver.find_element(By.XPATH, pw_input).send_keys("")

tomar_screenshot(driver, "inicio_vacio")
time.sleep(1)
driver.find_element(By.XPATH, btn_continue).click()
time.sleep(2)

try:
    error_message = driver.find_element(By.XPATH, '//*[@id="flash"]')
    tomar_screenshot(driver, "inicio_vacio")
    if "Campos obligatorios" in error_message.text:
        print(f"Test exitoso: {error_message.text}")
    else:
        print(f"Test fallido: Mensaje de de error no encontrado")
        
except Exception as e:
    print(f"Test fallido: Ocurrió un error - {e}")
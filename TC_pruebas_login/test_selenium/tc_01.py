from selenium import webdriver
from selenium.webdriver.common.by import By
from var import *
import time

counter = 1
def tomar_screenshot(driver, screen_name: str):
    global counter
    driver.save_screenshot(f"TC_pruebas_login/test_selenium/test_images/pruebas_01_{screen_name}_{counter}.png")
    counter += 1

driver = webdriver.Edge()
driver.get(link)
time.sleep(3)

tomar_screenshot(driver, "inicio_exitoso")
time.sleep(1)

driver.find_element(By.XPATH, uname_input).send_keys("tomsmith")
driver.find_element(By.XPATH, pw_input).send_keys("SuperSecretPassword!")

tomar_screenshot(driver, "inicio_exitoso")
time.sleep(1)
driver.find_element(By.XPATH, btn_continue).click()
time.sleep(2)

try:
    success_message = driver.find_element(By.XPATH, '//*[@id="content"]/div/h4')
    tomar_screenshot(driver, "inicio_exitoso")
    if "Welcome to the Secure Area. When you are done click logout below." in success_message.text:
        print(f"Test exitoso: {success_message.text}")
    else:
        print("Test fallido: Mensaje de éxito no encontrado")
        
except Exception as e:
    print(f"Test fallido: Ocurrió un error - {e}")
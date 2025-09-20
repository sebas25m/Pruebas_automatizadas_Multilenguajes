from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

id_screenshot = 0

def set_id_screenshot(driver):
    global id_screenshot 
    id_screenshot += 1
    driver.save_screenshot(f"Screenshot_qa/Toma_login_herokuapp_{id_screenshot}.png")
    

def test_succes_login(driver):
    time.sleep(2)
    set_id_screenshot(driver)

    username_input = driver.find_element(By.ID, "username")
    pw_input = driver.find_element(By.ID, "password")
    btn = driver.find_element(By.XPATH, '//*[@id="login"]/button')

    username_input.send_keys("tomsmith")
    pw_input.send_keys("SuperSecretPassword!")

    set_id_screenshot(driver)

    time.sleep(2)

    btn.click()

    time.sleep(2)
    
    succes_message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
    ).text
    time.sleep(2)
    set_id_screenshot(driver)
    print(f"✅ Login exitoso: {succes_message}")
    
def test_failed_login(driver):
    time.sleep(2)
    set_id_screenshot(driver)

    username_input = driver.find_element(By.ID, "username")
    pw_input = driver.find_element(By.ID, "password")
    btn = driver.find_element(By.XPATH, '//*[@id="login"]/button')

    username_input.send_keys("Mi_Prueba")
    pw_input.send_keys("HolaMundo!")

    set_id_screenshot(driver)

    time.sleep(2)

    btn.click()

    time.sleep(2)
    set_id_screenshot(driver)
    
    error_message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error"))
    ).text
    time.sleep(2)
    set_id_screenshot(driver)
    print(f"❌ Login fallido: {error_message}")


def close_driver(driver):
    driver.quit()


if __name__ == "__main__":
    driver = webdriver.Edge()

    driver.get("https://the-internet.herokuapp.com/login")

    test_failed_login(driver)
    
    test_succes_login(driver)

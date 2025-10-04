from playwright.sync_api import sync_playwright
from var import *

counter = 1

def tomar_screenshot(page, screen_name: str):
    global counter
    page.screenshot(path=f"TC_pruebas_login/test_playwright/test_images/pruebas_01_{screen_name}_{counter}.png")
    counter += 1

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) 
    page = browser.new_page()

    page.goto(link)
    page.wait_for_timeout(3000) 
    tomar_screenshot(page, "inicio_exitoso")

    page.locator(uname_input).fill("tomsmith")
    page.locator(pw_input).fill("SuperSecretPassword!")
    tomar_screenshot(page, "credenciales")

    page.locator(btn_continue).click()
    page.wait_for_timeout(2000)

    try:
        success_message = page.locator('//*[@id="content"]/div/h4')
        success_text = success_message.text_content()
        tomar_screenshot(page, "resultado")

        if "Welcome to the Secure Area. When you are done click logout below." in success_text:
            print(f"Test exitoso: {success_text}")
        else:
            print("Test fallido: Mensaje de éxito no encontrado")

    except Exception as e:
        print(f"Test fallido: Ocurrió un error - {e}")

    browser.close()

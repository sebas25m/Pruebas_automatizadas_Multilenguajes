from playwright.sync_api import sync_playwright
from var import *

counter = 1

def tomar_screenshot(page, screen_name: str):
    global counter
    page.screenshot(path=f"TC_pruebas_login/test_playwright/test_images/tc_03_{screen_name}_{counter}.png")
    counter += 1

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(link)
    page.wait_for_timeout(3000)
    tomar_screenshot(page, "inicio_vacio")

    page.locator(uname_input).fill("")
    page.locator(pw_input).fill("")
    tomar_screenshot(page, "campos_vacios")

    page.locator(btn_continue).click()
    page.wait_for_timeout(2000)

    try:
        error_message = page.locator('//*[@id="flash"]')
        error_text = error_message.text_content()
        tomar_screenshot(page, "resultado")

        if "Campos obligatorios" in error_text:
            print(f"Test exitoso: {error_text}")
        else:
            print("Test fallido: Mensaje de error no encontrado")
    except Exception as e:
        print(f"Test fallido: Ocurrió un error - {e}")

    browser.close()

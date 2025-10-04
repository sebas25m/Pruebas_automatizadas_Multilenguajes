from playwright.sync_api import sync_playwright
from var import *

counter = 1

def tomar_screenshot(page, screen_name: str):
    global counter
    page.screenshot(path=f"TC_pruebas_login/test_playwright/test_images/tc_04_{screen_name}_{counter}.png")
    counter += 1

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(link)
    page.wait_for_timeout(3000)
    tomar_screenshot(page, "logout_exitoso")

    page.locator(uname_input).fill("tomsmith")
    page.locator(pw_input).fill("SuperSecretPassword!")
    tomar_screenshot(page, "credenciales")

    page.locator(btn_continue).click()
    page.wait_for_timeout(2000)
    page.locator('//*[@id="content"]/div/h4')
    tomar_screenshot(page, "login_exitoso")

    try:
        btn_logout = page.locator('//*[@id="content"]/div/a/i')
        btn_logout.click()
        page.wait_for_timeout(2000)

        logout_text = page.locator('//*[@id="flash"]')
        text = logout_text.text_content()
        tomar_screenshot(page, "logout_exitoso")

        if "You logged out of the secure area!" in text:
            print(f"Test exitoso: {text}")
        else:
            print("Test fallido: Mensaje de éxito no encontrado")
    except Exception as e:
        print(f"Test fallido: Ocurrió un error - {e}")

    browser.close()

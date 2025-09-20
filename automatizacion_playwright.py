from playwright.sync_api import sync_playwright
import time
id_screenshot = 0

def set_id_screenshot(page):
    global id_screenshot 
    id_screenshot += 1
    page.screenshot(path=f"Screenshot_qa/Playwright/playwright_login_{id_screenshot}.png")

def test_succes_login(playwright):
    browser = playwright.chromium.launch(headless=False) 
    page = browser.new_page()

    page.goto("https://the-internet.herokuapp.com/login")
    time.sleep(2)
    set_id_screenshot(page)
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    set_id_screenshot(page)
    page.click('button[type="submit"]')
    time.sleep(2)
    success_message = page.wait_for_selector(".flash.success")
    set_id_screenshot(page)
    print("✅ Login exitoso:", success_message.inner_text())

    browser.close()
    
    
def test_falied_login(playwright):
    browser = playwright.chromium.launch(headless=False) 
    page = browser.new_page()

    page.goto("https://the-internet.herokuapp.com/login")
    time.sleep(2)
    set_id_screenshot(page)
    page.fill("#username", "Mi_Prueba")
    page.fill("#password", "HolaMundo!")
    set_id_screenshot(page)

    page.click('button[type="submit"]')
    time.sleep(2)
    
    error_message = page.wait_for_selector(".flash.error")
    set_id_screenshot(page)
    
    print(f"❌ Login fallido: {error_message.inner_text()}")

    browser.close()

with sync_playwright() as playwright:
    test_succes_login(playwright)
    test_falied_login(playwright)

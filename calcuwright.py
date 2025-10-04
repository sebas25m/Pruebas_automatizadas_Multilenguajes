import os, time
from playwright.sync_api import sync_playwright

os.makedirs("evidencias_playwright", exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    page.goto("https://testsheepnz.github.io/BasicCalculator.html")

    casos_prueba = [
        {"id": "TC01", "n1": "",     "n2": "",    "operacion": "Add", "extra": None},
        {"id": "TC02", "n1": "10",   "n2": "0",   "operacion": "Divide", "extra": None},
        {"id": "TC03", "n1": "abc",  "n2": "5",   "operacion": "Add", "extra": None},
        {"id": "TC04", "n1": "3,5",  "n2": "2",   "operacion": "Add", "extra": None},
        {"id": "TC05", "n1": "3.5",  "n2": "2,5", "operacion": "Add", "extra": None},
        {"id": "TC06", "n1": "10",   "n2": "5",   "operacion": "Add", "extra": None},
        {"id": "TC07", "n1": "3.8",  "n2": "5.3", "operacion": "Add", "extra": None},
        {"id": "TC08", "n1": "4.3",  "n2": "3.9", "operacion": "Add", "extra": "integers"}
    ]

    for caso in casos_prueba:
        page.fill("#number1Field", "")
        page.fill("#number2Field", "")
        if page.is_checked("#integerSelect"):
            page.click("#integerSelect")

        if caso["n1"]: page.fill("#number1Field", caso["n1"])
        if caso["n2"]: page.fill("#number2Field", caso["n2"])

        page.select_option("#selectOperationDropdown", label=caso["operacion"])

        if caso["extra"] == "integers":
            page.click("#integerSelect")

        page.click("#calculateButton")
        time.sleep(1)

        resultado = page.input_value("#numberAnswerField")
        print(f"✅ {caso['id']}: Resultado obtenido = {resultado}")

        file_name = f"evidencias_playwright/{caso['id']}_{resultado or 'vacio'}.png"
        page.screenshot(path=file_name)
        print(f"📸 Captura guardada: {file_name}")

        page.reload()

    time.sleep(3)
    browser.close()

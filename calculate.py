import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

os.makedirs("evidencias_selenium", exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://testsheepnz.github.io/BasicCalculator.html")

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
    # Limpiar campos
    driver.find_element(By.ID, "number1Field").clear()
    driver.find_element(By.ID, "number2Field").clear()
    driver.find_element(By.ID, "integerSelect").click() if driver.find_element(By.ID, "integerSelect").is_selected() else None

    # Ingresar datos
    if caso["n1"]: driver.find_element(By.ID, "number1Field").send_keys(caso["n1"])
    if caso["n2"]: driver.find_element(By.ID, "number2Field").send_keys(caso["n2"])

    # Seleccionar operación
    driver.find_element(By.ID, "selectOperationDropdown").send_keys(caso["operacion"])

    # Integers Only si aplica
    if caso["extra"] == "integers":
        driver.find_element(By.ID, "integerSelect").click()

    # Calcular
    driver.find_element(By.ID, "calculateButton").click()
    time.sleep(2)

    # Resultado
    resultado = driver.find_element(By.ID, "numberAnswerField").get_attribute("value")
    print(f"✅ {caso['id']}: Resultado obtenido = {resultado}")

    # Captura
    file_name = f"evidencias_selenium/{caso['id']}_{resultado or 'vacio'}.png"
    driver.save_screenshot(file_name)
    print(f"📸 Captura guardada: {file_name}")

    driver.refresh()

time.sleep(3)
driver.quit()


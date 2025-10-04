const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
  // Nombre de carpeta igual que en Selenium y Playwright
  const folder = "evidencias_puppeteer";
  if (!fs.existsSync(folder)) {
    fs.mkdirSync(folder);
  }

  const browser = await puppeteer.launch({
    headless: false, 
    defaultViewport: null 
  });

  const page = await browser.newPage();
  await page.goto("https://testsheepnz.github.io/BasicCalculator.html");

  // Casos de prueba
  const casosPrueba = [
    { id: "TC01", n1: "",     n2: "",    operacion: "0", extra: null },
    { id: "TC02", n1: "10",   n2: "0",   operacion: "3", extra: null },
    { id: "TC03", n1: "abc",  n2: "5",   operacion: "0", extra: null },
    { id: "TC04", n1: "3,5",  n2: "2",   operacion: "0", extra: null },
    { id: "TC05", n1: "3.5",  n2: "2,5", operacion: "0", extra: null },
    { id: "TC06", n1: "10",   n2: "5",   operacion: "0", extra: null },
    { id: "TC07", n1: "3.8",  n2: "5.3", operacion: "0", extra: null },
    { id: "TC08", n1: "4.3",  n2: "3.9", operacion: "0", extra: "integers" }
  ];

  for (const caso of casosPrueba) {

    // Limpiar campos y desmarcar Integers Only
    await page.evaluate(() => {
      document.querySelector("#number1Field").value = "";
      document.querySelector("#number2Field").value = "";
      document.querySelector("#integerSelect").checked = false;
    });

    // Llenar valores
    if (caso.n1 !== "") await page.type("#number1Field", caso.n1);
    if (caso.n2 !== "") await page.type("#number2Field", caso.n2);

    // Seleccionar operación
    await page.select("#selectOperationDropdown", caso.operacion);

    // Activar Integers Only si aplica
    if (caso.extra === "integers") {
      await page.click("#integerSelect");
    }

    // Calcular
    await page.click("#calculateButton");

    // Pequeña pausa para que el resultado se procese
    await new Promise(r => setTimeout(r, 1200));

    // Obtener resultado
    const resultado = await page.$eval("#numberAnswerField", el => el.value);
    console.log(`✅ ${caso.id}: Resultado obtenido = ${resultado}`);

    // Guardar captura en la carpeta correcta
    const fileName = `${folder}/${caso.id}_${resultado || "vacio"}.png`;
    await page.screenshot({ path: fileName });
    console.log(`📸 Captura guardada: ${fileName}`);

    // Recargar antes del siguiente caso
    await page.reload();
    await new Promise(r => setTimeout(r, 1000));
  }

  console.log("Todas las pruebas de Puppeteer finalizadas.");
  await new Promise(r => setTimeout(r, 3000));
  await browser.close();
})();

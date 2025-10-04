const puppeteer = require('puppeteer');

// Variables
const link = "https://the-internet.herokuapp.com/login";
const uname_input = '#username';
const pw_input = '#password';
const btn_continue = '#login button i';

let counter = 1;

async function tomar_screenshot(page, screen_name) {
    await page.screenshot({
        path: `test_images/tc_03_${screen_name}_${counter}.png`
    });
    counter++;
}

async function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

(async () => {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();

    await page.goto(link, { waitUntil: 'networkidle2' });
    await sleep(3000);
    await tomar_screenshot(page, "inicio_vacio");

    // Username vacío
    await page.type(uname_input, "");

    // Password vacío
    await page.type(pw_input, "");
    await tomar_screenshot(page, "campos_vacios");

    // Clic en login
    await page.click(btn_continue);
    await sleep(2000);

    try {
        const error_message = await page.$('#flash');
        if (error_message) {
            const error_text = await page.evaluate(el => el.textContent, error_message);
            await tomar_screenshot(page, "resultado");

            if (error_text.includes("Campos obligatorios")) {
                console.log(`✅ Test exitoso: ${error_text}`);
            } else {
                console.log("❌ Test fallido: Mensaje de error no encontrado");
            }
        } else {
            console.log("❌ Test fallido: No se encontró el mensaje de error");
        }
    } catch (e) {
        console.log(`❌ Test fallido: Ocurrió un error - ${e}`);
    }

    await browser.close();
})();

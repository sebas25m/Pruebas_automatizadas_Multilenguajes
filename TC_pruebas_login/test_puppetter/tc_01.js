const puppeteer = require('puppeteer');

// Variables
const link = "https://the-internet.herokuapp.com/login";
const uname_input = '#username';
const pw_input = '#password';
const btn_continue = '#login button i';

let counter = 1;

async function tomar_screenshot(page, screen_name) {
    await page.screenshot({
        path: `test_images/pruebas_01_${screen_name}_${counter}.png`
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
    await tomar_screenshot(page, "inicio_exitoso");

    // Username
    await page.type(uname_input, "tomsmith");

    // Password
    await page.type(pw_input, "SuperSecretPassword!");
    await tomar_screenshot(page, "credenciales");

    // Botón login
    await page.click(btn_continue);
    await sleep(2000);

    try {
        const success_message = await page.$('#content h4');
        if (success_message) {
            const success_text = await page.evaluate(el => el.textContent, success_message);
            await tomar_screenshot(page, "resultado");

            if (success_text.includes("Welcome to the Secure Area. When you are done click logout below.")) {
                console.log(`✅ Test exitoso: ${success_text}`);
            } else {
                console.log("❌ Test fallido: Mensaje de éxito no encontrado");
            }
        } else {
            console.log("❌ Test fallido: No se encontró el mensaje de éxito");
        }
    } catch (e) {
        console.log(`❌ Test fallido: Ocurrió un error - ${e}`);
    }

    await browser.close();
})();

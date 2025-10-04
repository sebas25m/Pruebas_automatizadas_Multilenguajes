const puppeteer = require('puppeteer');

// Variables
const link = "https://the-internet.herokuapp.com/login";
const uname_input = '#username';
const pw_input = '#password';
const btn_continue = '#login button i';
const btn_logout = '#content a i';
const flash_message = '#flash';
const secure_area = '#content h4';

let counter = 1;

async function tomar_screenshot(page, screen_name) {
    await page.screenshot({
        path: `test_images/tc_04_${screen_name}_${counter}.png`
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
    await tomar_screenshot(page, "inicio");

    // Login con credenciales válidas
    await page.type(uname_input, "tomsmith");
    await page.type(pw_input, "SuperSecretPassword!");
    await tomar_screenshot(page, "credenciales");

    await page.click(btn_continue);
    await sleep(2000);

    // Verificar login exitoso
    await page.$(secure_area);
    await tomar_screenshot(page, "login_exitoso");

    try {
        // Logout
        await page.click(btn_logout);
        await sleep(2000);

        const logout_message = await page.$(flash_message);
        if (logout_message) {
            const text = await page.evaluate(el => el.textContent, logout_message);
            await tomar_screenshot(page, "logout_exitoso");

            if (text.includes("You logged out of the secure area!")) {
                console.log(`✅ Test exitoso: ${text}`);
            } else {
                console.log("❌ Test fallido: Mensaje de éxito no encontrado");
            }
        } else {
            console.log("❌ Test fallido: No se encontró el mensaje de logout");
        }
    } catch (e) {
        console.log(`❌ Test fallido: Ocurrió un error - ${e}`);
    }

    await browser.close();
})();

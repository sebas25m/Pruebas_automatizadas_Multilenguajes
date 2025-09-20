const puppeteer = require('puppeteer');

let screenshotId = 0;

async function takeScreenshot(page) {
  screenshotId += 1;
  const path = `puppeteer_screenshot_failed_${screenshotId}.png`;
  await page.screenshot({ path });
}

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  await page.goto('https://the-internet.herokuapp.com/login');

  await takeScreenshot(page);

  await page.type('#username', 'Mi_Prueba');
  await page.type('#password', 'HolaMundo!');

  await takeScreenshot(page);

  await page.click('button[type="submit"]');

  await page.waitForSelector('.flash.error');
  const mensaje = await page.$eval('.flash.error', el => el.textContent);
  console.log('❌ Login fallido: ', mensaje.trim());

  await takeScreenshot(page);

  await browser.close();
})();
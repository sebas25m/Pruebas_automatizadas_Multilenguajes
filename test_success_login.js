const puppeteer = require('puppeteer');

let screenshotId = 0;

async function takeScreenshot(page) {
  screenshotId += 1;
  const path = `puppeteer_screenshot_success_${screenshotId}.png`;
  await page.screenshot({ path });
}

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  await page.goto('https://the-internet.herokuapp.com/login');
  await takeScreenshot(page);

  await page.type('#username', 'tomsmith');
  await page.type('#password', 'SuperSecretPassword!');
  await takeScreenshot(page);

  await page.click('button[type="submit"]');

  
  await page.waitForSelector('.flash.success');
  await takeScreenshot(page);
  const mensaje = await page.$eval('.flash.success', el => el.textContent);
  console.log('✅ Login exitoso:', mensaje.trim());

  await page.screenshot({ path: 'screenshot_login.png' });
  await browser.close();
})();
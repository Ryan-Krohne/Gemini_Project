from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time



# Create Chrome options with incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")


def browse_canva():

    driver = webdriver.Chrome(options=chrome_options)
    
    
    try:
        # Navigate to Canva
        driver.maximize_window()
        driver.get('https://www.canva.com')


        time.sleep(1)

        # Locate the login button by its text and click on it
        login_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Log in"]'))
        )
        login_btn.click()


        login_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[normalize-space()="Continue with email"]'))
        )
        login_btn.click()

        time.sleep(1)

        driver.execute_script('''

            document.activeElement.value += 'test';

            // Simulate hitting Enter key
            var event = new KeyboardEvent('keydown', {
                key: 'Enter',
                bubbles: true,
                cancelable: true,
            });
            document.activeElement.dispatchEvent(event);
        ''')


        # Wait for 3 seconds (optional)
        time.sleep(300)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    browse_canva()

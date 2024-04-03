import undetected_chromedriver as uc

# this is a test push

# Initialize Chrome driver with disabled SSL verification
driver = uc.Chrome(headless=True)
driver.get('https://nowsecure.nl')
driver.save_screenshot('nowsecure.png')





from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configure headless Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enables headless mode

# Create new Chrome session with options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to Google
driver.get("https://www.google.com/")

# Wait for the page to load (optional, adjust based on your needs)
# You might need to adjust this wait time depending on your internet speed
# and how long it takes for Google to fully load
driver.implicitly_wait(10)  # Wait for up to 10 seconds

# Capture screenshot
screenshot_name = "google_screenshot.png"
driver.save_screenshot(screenshot_name)

# Close the browser
driver.quit()

print(f"Screenshot saved as: {screenshot_name}")

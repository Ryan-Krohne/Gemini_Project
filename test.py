import undetected_chromedriver as uc


# Initialize Chrome driver with disabled SSL verification
driver = uc.Chrome(headless=True)
driver.get('https://nowsecure.nl')
driver.save_screenshot('nowsecure.png')

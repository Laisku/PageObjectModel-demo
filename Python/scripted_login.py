# Make Selenium available to Python
from selenium import webdriver 
# Allow us to access the By function which we’ll use later. See note 1
from selenium.webdriver.common.by import By
# we need this to use "sleep" (pause)
import time
 
# Open a Chrome session. Relies on Chromedriver. See note 2
driver = webdriver.Chrome() 
 
# Open the web page
driver.get("https://the-internet.herokuapp.com/login") 
 
# Find the username field by ID and send a value
driver.find_element(By.ID, "username").send_keys("tomsmith")
 
# Find the password field byID and send a value
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!") 
 
# Wait for 3 seconds
time.sleep(3)
 
# Find the Submit button using classes (the "." prefix means "class"), convert it to a CSS selector and then click it
driver.find_element(By.CSS_SELECTOR, ".fa.fa-2x.fa-sign-in").click() 
 
# Wait for 3 seconds
time.sleep(3)
 
# Close the session
driver.quit()
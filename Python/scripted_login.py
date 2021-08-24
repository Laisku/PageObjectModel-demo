from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
 
driver = webdriver.Chrome() 
driver.get("https://the-internet.herokuapp.com/login") 
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!") 
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".fa.fa-2x.fa-sign-in").click() 
time.sleep(3)
driver.quit()
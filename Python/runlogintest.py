from selenium import webdriver
from selenium.webdriver.common.by import By
from loginpage import *


def setup():
    return webdriver.Chrome()
 
def logintest():
    driver = setup()
 
    driver.get("https://the-internet.herokuapp.com/login")
 
    login_form = Login(driver)
    login_form.login()
    driver.quit()
 
if __name__ == "__main__":
    logintest()
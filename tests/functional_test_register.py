# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# create webdriver object
driver = webdriver.Chrome()



def register(driver, username, password):
    driver.get('http://localhost:5000/register')  # URL to the registration page

    # Wait for the registration page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )

    # Find the input elements by their name attributes
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    

    # Fill in the username and password
    username_input.send_keys("sumon")
    password_input.send_keys("1234")
    

    # Submit the registration form
    register_button = driver.find_element(By.XPATH,'/html/body/div/form/button')
    register_button.click()

def login(Login):
    Login = driver.find_element(By.XPATH,'/html/body/div/p/a')
    Login.click()
    if Login.click ==driver.get('http://localhost:5000/login'):
        print('We can enter Login page successfully')
    else:
        print('we cannot enter Login page successfully')







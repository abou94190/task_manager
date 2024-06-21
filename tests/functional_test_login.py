# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# create webdriver object
driver = webdriver.Chrome()
 



# Function to test login functionality
def test_login(username, password):
    
    driver.get('http://localhost:5000/login')

    # Wait for the page to load
    time.sleep(2)

    try:
        # Find the username input element and enter the username
        username_input =driver.find_element(By.XPATH,'/html/body/div/form/input[1]')
        username_input.send_keys("amir")

        # Find the password input element and enter the password
        password_input = driver.find_element(By.XPATH, '/html/body/div/form/input[2]')
        password_input.send_keys("1234")

        # Find the login button and click it
        login_button = driver.find_element(By.XPATH, '/html/body/div/form/button')
        login_button.click()

        # Wait for the login process to complete
        time.sleep(2)

        # Check if the login was successful
        if login_button.click ==driver.get('http://localhost:5000/index'):
             print('Login successful')
        
        else:
               print('Login failed')
               time.sleep(2)
               driver.get('http://localhost:5000/register')
    

    finally:
        # Close the browser
        driver.quit()

# Test cases
def run_tests():
    # Test with valid credentials
    print("Testing with valid credentials:")
    test_login('valid_username', 'valid_password')

    # Test with invalid credentials
    print("\nTesting with invalid credentials:")
    test_login('invalid_username', 'invalid_password')

# Run the tests
if __name__ == "__main__":
    run_tests()
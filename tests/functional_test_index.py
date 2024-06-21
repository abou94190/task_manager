# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
# create webdriver object
driver = webdriver.Chrome()



def login(driver, username, password):
    driver.get('http://localhost:5000/login')  # URL to the login page

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/div/form/input[1]'))
    )

    username_input =driver.find_element(By.XPATH,'/html/body/div/form/input[1]')
    username_input.send_keys("sumon")

        # Find the password input element and enter the password
    password_input = driver.find_element(By.XPATH, '/html/body/div/form/input[2]')
    password_input.send_keys("1234")

        # Find the login button and click it
    login_button = driver.find_element(By.XPATH, '/html/body/div/form/button')
    login_button.click()

time.sleep(2)
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/head/title'))
    )


def add_task(task_id, task_description, task_priority):
    driver.get('http://localhost:5000/index')
    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'task_id'))
    )
   


    

    # Find the input elements by their name or id attributes
    task_id_input = driver.find_element(By.NAME, 'task_id')
    task_description_input = driver.find_element(By.NAME, 'description')
    task_priority_dropdown =Select(driver.find_element(By.NAME, 'priority'))

    # Fill in the task ID
    task_id_input.send_keys("15")

    # Fill in the task description
    task_description_input.send_keys("FOOTBALL")

    # Select an option from the dropdown
    task_priority_dropdown.select_by_visible_text("low")

    # Submit the form
    submit_button = driver.find_element(By.XPATH, '/html/body/div/form/button')
    submit_button.click()
    time.sleep(2)

# Wait for the task table to be updated
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/ul'))
    )


def verify_task(task_id,description,priority):
    task_table = driver.find_element(By.XPATH, '/html/body/div/ul')
    rows = task_table.find_elements(By.XPATH, '/html/body/div/ul/li[1]')

    # Verify the task is in the table
    task_found = False
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, 'td')
        if columns and columns[0].text == task_id and columns[1].text == description and columns[2].text == priority:
            task_found = True
            break

    assert task_found, "Task was not found in the task table"

def logout(driver):
    logout_button = driver.find_element(By.XPATH, '/html/body/div/a')
    logout_button.click()
    # Wait for the login page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )

  
def test_task_manager():
    

    try:
        # Login
        login(driver, 'sumon', '1234')

        # Add task
        add_task(driver, '15', 'FOOTBALL', 'low')

        # Verify task
        verify_task(driver, '15', 'FOOTBALL', 'low')

        # Logout
        logout(driver)

    finally:
        # Close the browser
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_task_manager()

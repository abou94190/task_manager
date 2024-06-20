# Task Manager Project

## Introduction
The Task Manager project is a web application designed to help users manage their tasks effectively. It includes functionalities for user registration, login,task management. This project also integrates Selenium for automated functional testing of various features.

## Features
- **User Management:**
  - User Registration
  - User Login
  - index for Task Management
- **Task Management:**
  - Create Tasks
  - View Tasks
  - Delete Tasks
  - Mark Tasks as Complete
  
- **Task Prioritization:**
  - Set task priority (High, Medium, Low)

## Prerequisites
- Python 3.x
- Selenium WebDriver
- ChromeDriver (or other browser driver)
- Flask (for running the web application)
- Virtual Environment (optional but recommended)

## Setup Instructions
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/task_manager.git
    cd task_manager
    ```

2. **Create and Activate a Virtual Environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Required Packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask Application:**
    ```bash
    export FLASK_APP=app.py
    flask run
    ```

## Usage
Open your web browser and navigate to `http://127.0.0.1:5000` to access the Task Manager application.

## Running Selenium Tests
This project includes Selenium tests to automate the functional testing of user registration, login, and task management. Below are the instructions to run these tests.

### Prerequisites for Selenium Tests
- Ensure you have Google Chrome installed.
- Download the ChromeDriver from [here](https://sites.google.com/chromium.org/driver/downloads) and place it in your PATH or specify the path in the script.

### Selenium Test Script
The test script is located in the `tests` directory.

### Example Test Script
Here's an example of a Selenium test script for user task management(index):

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

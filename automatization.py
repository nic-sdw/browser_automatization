import numpy as np
import pandas as pd
import selenium as sn
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv('config.env')

link = os.getenv('LINK')
link_recuperacao = os.getenv('LINKREC')
user = os.getenv('USER')
pswd = os.getenv('PASSWORD')

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
driver.get(link)

try:

# Login screen setup

    # Wait for the login field to be visible and input the username
    login = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'txtLogin'))
    )
    login.send_keys(user)

    # Wait for the password field to be visible and input the password
    password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'txtSenha'))
    )
    password.send_keys(pswd)

    # Wait for the login button to be clickable and click it
    btn_enter = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'btnOk'))
    )
    btn_enter.click()

    # Here we go to the other page after logging into the system.
    driver.get(link_recuperacao)

    first_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "td.MenuItem[id='Menu1-menuItem000']"))
    )
    first_item.click()

    second_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "td.MenuItem[id=Menu1-menuItem000-subMenu-menuItem000]"))
    )
    second_item.click()

    # Wait for the iframe to load
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'conteudo'))
    )

    # Switch context to iframe
    driver.switch_to.frame(iframe)

    # Wait until the element is loaded and visible
    rb_planejados = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'rblApontamento_0')))

    rb_planejados.click()

    WebDriverWait(driver, 10).until(
        lambda driver: driver.execute_script(
            'return document.readyState') == 'complete'
    )

    time.sleep(3)

    # Wait until the href element is loaded and ready
    table = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'olvOrdemServico'))
    )

    table = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'olvOrdemServico'))
    )
    tbody = table.find_element(By.TAG_NAME, 'tbody')
    even_rows = tbody.find_elements(By.CSS_SELECTOR, 'tr.even')
    cell = even_rows[0].find_elements(By.TAG_NAME, 'td')[1]
    link = cell.find_element(By.TAG_NAME, 'a')
    link.click()

except Exception as e:
    print(f"Error during navigation: {str(e)}")
    driver.quit()

# Wait for a few seconds to observe the action


# Close the browser
finally:
    time.sleep(10)
    driver.quit()
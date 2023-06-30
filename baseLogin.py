import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from POM.loginPage import loginPage
from POM.data import inputan


def test_login(driver, self):
    # steps
    driver.find_element(*loginPage.addUsername).send_keys(inputan.valid_username) # isi email
    #driver.find_element(By.ID,loginPage.passw "password").send_keys("secret_sauce") # isi password
    driver.find_element(By.ID,loginPage.passw).send_keys(inputan.valid_passw) # isi password

    driver.find_element(By.CLASS_NAME, "submit-button.btn_action").click()
    
    # validasi
    response_data = driver.find_element(By.CLASS_NAME,"title").text
    self.assertIn('Products', response_data)

def test_login2(driver, self, username, password):
    # steps
    driver.find_element(By.CSS_SELECTOR,"[data-test='username']").send_keys(username) # isi email
    driver.find_element(By.ID,"password").send_keys(password) # isi password
    driver.find_element(By.CLASS_NAME, "submit-button.btn_action").click()
    
        
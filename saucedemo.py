
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import baseLogin
from POM.loginPage import loginPage
from POM.data import inputan

class TestLogin(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome()
        #self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
 
    def test_a_success_login(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        """driver.find_element(By.CSS_SELECTOR,"[data-test='username']").send_keys("standard_user") # isi email
        #driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        #driver.find_element(By.CLASS_NAME,"input_error.from_input").send_keys("standard_user") # isi email
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        #driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.CLASS_NAME, "submit-button.btn_action").click()"""
        baseLogin.test_login(driver, self)
        #validasi
        response_data = driver.find_element(By.CLASS_NAME, loginPage.loginTitle).text
        self.assertIn('Products', response_data)

    def test_a_failed_login(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        """driver.find_element(By.ID,"user-name").send_keys("salahuser") # isi username
        driver.find_element(By.ID,"password").send_keys("salahpasw") # isi password
        driver.find_element(By.ID, "login-button").click()"""
        baseLogin.test_login2(driver, self, inputan.invalid_username, inputan.invalid_passw)
        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,loginPage.errorMsg).text
        self.assertIn('Epic sadface: Username and password do not match any user in this service', response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()

import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import baseLogin
from POM.cartPage import cartPage

class TestAddtoCart(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = "https://www.saucedemo.com/"
    def test_add_to_cart(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        baseLogin.test_login(driver, self) #memanggil def test_login
        

        driver.find_element(*cartPage.addBackpack).click()
        cart = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
        self.assertEqual(cart, '1')
        driver.find_element(By.CLASS_NAME,"shopping_cart_badge").click
         
        #validasi
        url = driver.current_url
        self.assertIn('/inventory.html', url)
        driver.find_element(By.CLASS_NAME, "inventory_item_name")


    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
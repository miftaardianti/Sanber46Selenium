from selenium.webdriver.common.by import By
class loginPage():
    username = "user-name"
    passw = "password"
    errorMsg = "[data-test='error']"
    loginTitle = "title"

    #addBackpack = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']") 
    addUsername = By.CSS_SELECTOR,"[data-test='username']"
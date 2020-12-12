from pageObjects.CheckoutPage import CheckOutPage
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    search = (By.CLASS_NAME, "search-keyword")
    items = (By.CSS_SELECTOR, "div[class='product'] h4")
    itemsCart = (By.CSS_SELECTOR, "[class='product'] button")
    itemsQuantity = (By.CSS_SELECTOR, "[class='product'] a[class='increment']")
    cartIcon = (By.CSS_SELECTOR, "[class='cart-icon']")
    cartCheckOut = (By.XPATH, "//button[contains(text(), 'PROCEED TO')]")

    def searchItem(self):
        return self.driver.find_element(*HomePage.search)

    def getItems(self):
        return self.driver.find_elements(*HomePage.items)

    def getItemsCart(self):
        return self.driver.find_elements(*HomePage.itemsCart)

    def getItemsQuantity(self):
        return self.driver.find_elements(*HomePage.itemsQuantity)

    def getCartIcon(self):
        return self.driver.find_element(*HomePage.cartIcon)

    def getCartCheckOut(self):
        self.driver.find_element(*HomePage.cartCheckOut).click()
        checkOutPage = CheckOutPage(self.driver)
        return CheckOutPage







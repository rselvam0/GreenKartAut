from pageObjects.ConfirmPage import ConfirmPage
from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    chkOutItem = (By.CSS_SELECTOR, "p.product-name")
    promoCode = (By.CSS_SELECTOR, "input.promoCode")
    promoButton = (By.CLASS_NAME, "promoBtn")
    originalAmt = (By.CSS_SELECTOR, "[class='totAmt']")
    discountedAmt = (By.CLASS_NAME, "discountAmt")
    placeOrder = (By.XPATH, "//button[contains(text(), 'Place Order')]")

    def getChkOutItem(self):
        return self.driver.find_elements(*CheckOutPage.chkOutItem)

    def getPromoCode(self):
        return self.driver.find_element(*CheckOutPage.promoCode)

    def getPromoButton(self):
        return self.driver.find_element(*CheckOutPage.promoButton)

    def getOriginalAmt(self):
        return self.driver.find_element(*CheckOutPage.originalAmt)

    def getDiscountedAmt(self):
        return self.driver.find_element(*CheckOutPage.discountedAmt)

    def getPlaceOrder(self):
        self.driver.find_element(*CheckOutPage.placeOrder).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage



















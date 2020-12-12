from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    countryDropdown = (By.XPATH, "//select")
    checkBox = (By.CSS_SELECTOR, "input.chkAgree")
    proceed = (By.XPATH, "//button[contains(text(),'Proceed')]")

    def getCountryDropdown(self):
        return self.driver.find_element(*ConfirmPage.countryDropdown)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getProceedBtn(self):
        return self.driver.find_element(*ConfirmPage.proceed)








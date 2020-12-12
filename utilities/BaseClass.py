import inspect
import logging
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def checkLinkPresence(self):
        wait = WebDriverWait(self.driver, 8)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))

    def checkPromoInfo(self):
        wait = WebDriverWait(self.driver, 8)
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))

    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)


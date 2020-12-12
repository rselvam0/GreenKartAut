import pytest
from TestData.HomePageData import HomePageData
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utilities.BaseClass import BaseClass


class TestGreenCart(BaseClass):
    def test_GreenKartE2E(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        searchItem = homepage.searchItem().send_keys(getData["searchKeyWord"])
        log.info("getting the vegetable names: ")
        items = homepage.getItems()
        assert len(items) == 2
        list1 = []
        list2 = []
        i = -1
        for veg in items:
            i = i + 1
            product_name = veg.text
            log.info(product_name)
            list1.append(product_name)
            if not product_name == getData["productID"]:
                homepage.getItemsQuantity()[i].click()
                homepage.getItemsCart()[i].click()
            else:
                homepage.getItemsCart()[i].click()
        print(list1)

        homepage.getCartIcon().click()
        homepage.getCartCheckOut()

        self.checkLinkPresence()
        checkOutPage = CheckOutPage(self.driver)

        checkout_items = checkOutPage.getChkOutItem()
        for item in checkout_items:
            list2.append(item.text)
        print(list2)
        assert list1 == list2

        checkOutPage.getPromoCode().send_keys(getData["promoCode"])
        checkOutPage.getPromoButton().click()

        self.checkPromoInfo()

        original_amount = checkOutPage.getOriginalAmt().text
        discounted_amount = checkOutPage.getDiscountedAmt().text
        log.info("Total Amount is: " + original_amount)
        log.info("Discounted Amount is: " + discounted_amount)
        assert int(original_amount) > float(discounted_amount)

        checkOutPage.getPlaceOrder()

        confirmationPage = ConfirmPage(self.driver)

        dropdown = Select(confirmationPage.getCountryDropdown())
        dropdown.select_by_visible_text("Australia")
        confirmationPage.getCheckBox().click()

        confirmationPage.getProceedBtn().click()
        assert self.driver.title == "GreenKart - veg and fruits kart"

        self.driver.get_screenshot_as_file("E:/Tech bite/4_Selenium_Udemy/GreenKartConf.png")

    @pytest.fixture(params=HomePageData.getTestDataGK())
    def getData(self, request):
        return request.param




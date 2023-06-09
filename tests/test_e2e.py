import pytest
from selenium import webdriver
import time

# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        self.driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']").click()
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()

        self.driver.find_element(By.ID, "country").send_keys("ind")

        # Explicit Wait Implementation
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()

        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        successMessage = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        print(successMessage)

        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in successMessage


from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardsName = (By.XPATH, "//div/h4/a")
    cardFooter = (By.CSS_SELECTOR, ".btn.btn-info")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardsName(self):
        return self.driver.find_elements(*CheckOutPage.cardsName)

    def getCardFooter(self):
        return self.driver.find_element(*CheckOutPage.cardFooter)

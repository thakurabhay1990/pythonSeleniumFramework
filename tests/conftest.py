import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()

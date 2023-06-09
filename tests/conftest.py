import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service


# Declared and initialized a run time variable below for command line terminal
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    # to retrieve Command line value
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("/Users/abhaythakur/Downloads/drivers/geckodriver")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "ie":
        service_obj = Service("/Users/abhaythakur/Downloads/drivers/msedgedriver")
        driver = webdriver.Edge(service=service_obj)

    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()

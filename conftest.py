import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

@pytest.fixture(scope='function')
def driver():
    driver_path = Service('C:\geckodriver.exe')
    driver = webdriver.Firefox(service= driver_path)
    driver.maximize_window()
    yield driver
    driver.quit()



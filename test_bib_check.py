import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def chrome_driver_settings():
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)


@pytest.fixture()
def browserdriver():
    driver = chrome_driver_settings()
    driver.get("https://secure.onreg.com/onreg2/bibexchange/?eventid=6736&language=us")
    return driver


def test_bib_check(browserdriver):
    WebDriverWait(browserdriver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[contains(text(), 'There are currently no race numbers for sale. Try again later.')]")))

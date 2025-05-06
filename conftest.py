import pytest
from selenium import webdriver


# Инициализируем драйвер Firefox
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

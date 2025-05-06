from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Ждем, пока элемент появится и возвращаем его
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    # Ждем, пока элемент станет кликабельным и нажимаем на него
    def click_on_element(self, locator):
        element = (WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator)))
        element.click()

    # Получаем текст элемента и возвращаем его
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    # Переходим по полученному url
    def go_to_url(self, url):
        self.driver.get(url)

    # Прокручиваем страницу до выбранного элемента
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    # Прокручиваем страницу до конца
    def scroll_down(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')




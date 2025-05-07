import allure
from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators import header_locators as locators

class Header(BasePage):
    @allure.step("Кликаем на логотип Яндекса")
    def click_on_yandex_logo(self):
        self.click_on_element(locators.logo_yandex_locator)

    @allure.step("Кликаем на логотип Самоката")
    def click_on_samokat_logo(self):
        self.click_on_element(locators.logo_samokat_locator)

    @allure.step("Переходим на последнюю открытую вкладку")
    def go_to_the_last_open_page(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Проверяем, что мы на странице яндекса")
    def check_is_location_on_yandex_page(self):
        try:
            self.find_element_with_wait(locators.check_redirect_yandex_locator)
            return True
        except TimeoutException:
            return False


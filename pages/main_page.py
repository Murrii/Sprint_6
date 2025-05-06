import allure
from pages.base_page import BasePage
import locators.main_page_locators as locators
from data import main_page_url as url


class MainPage(BasePage):
    @allure.step('Открываем Главную страницу')
    def open_main_page(self):
        self.driver.get(url)

    @allure.step('Кликаем на вопрос {num}')
    def click_to_question(self, num):
        final_question_locator = self.format_locator(locators.question_locator, num)
        self.click_on_element(final_question_locator)

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, num):
        final_answer_locator = self.format_locator(locators.answer_locator, num)
        return self.get_text_from_element(final_answer_locator)

    @allure.step("Прокручиваем страницу до последнего вопроса и ждем, пока все загрузится")
    def scroll_to_down(self):
        self.scroll_down()
        self.find_element_with_wait(locators.scroll_locator)

    # статический метод для форматирования локаторов
    @staticmethod
    def format_locator(locator, num):
        by, locator_for_format = locator
        format_locator = locator_for_format.format(num)
        return by, format_locator

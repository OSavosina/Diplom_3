from page_object.base_page import BasePage
from locators import Locators
from constants import UserFieldsCollection
import allure


class PageProfile(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход на форму авторизации')
    def go_to_form_login(self):
        self.find_element_base(locator=Locators.locator_button_user_profile, time=2).click()
        return self.get_current_url()

    @allure.step('Заполнение формы логина')
    def send_form_login(self, data):
        self.find_element_base(locator=Locators.locator_form_login_field_email, time=2).send_keys(data[UserFieldsCollection.EMAIL])
        self.find_element_base(locator=Locators.locator_form_login_field_password, time=2).send_keys(data[UserFieldsCollection.PASSWORD])
        self.find_element_base(locator=Locators.locator_form_login_button_enter, time=2).click()
        self.find_element_base(locator=Locators.locator_button_user_profile, time=2).is_displayed()

    @allure.step('Переход в раздел история заказов')
    def go_to_orders_history(self):
        self.find_element_base(locator=Locators.locator_link_order_history, time=2).click()

    @allure.step('Выход из аккаунта')
    def logout(self):
        self.find_element_base(locator=Locators.locator_form_login_button_exit, time=2).click()
        self.find_element_base(locator=Locators.locator_form_login_title_exit, time=2).is_displayed()

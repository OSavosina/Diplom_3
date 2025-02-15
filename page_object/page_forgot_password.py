from page_object.base_page import BasePage
from locators import Locators
import allure


class PageForgotPassword(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход на страницу логина')
    def go_to_form_login(self):
        self.find_element_base(locator=Locators.locator_button_user_profile, time=2).click()
        return self.get_current_url()


    @allure.step('Переход на страницу восстановления пароля')
    def go_to_page_forgot_password(self):
        self.find_element_base(locator=Locators.locator_link_forgot_password, time=2).click()
        return self.get_current_url()


    @allure.step('Переход на форму обновления пароля')
    def go_to_page_reset_password(self):
        self.find_element_base(locator=Locators.locator_button_forgot_password, time=2).click()
        self.find_element_base(locator=Locators.locator_field_type_password, time=2).is_displayed()
        return self.get_current_url()

    @allure.step('Заполнение поля email')
    def complete_field_email(self, email):
        self.find_element_base(locator=Locators.locator_field_email, time=2).send_keys(email)

    @allure.step('Проверка кнопки скрыть/показать пароль')
    def check_button_show_password(self, password):
        self.find_element_base(locator=Locators.locator_field_type_password, time=2).send_keys(password)
        self.find_element_base(locator=Locators.locator_icon_show_password, time=2).click()
        return self.find_element_base(locator=Locators.locator_field_type_text, time=2).is_displayed()

from page_object.page_forgot_password import PageForgotPassword
from constants import PageUrl
from helpers.helpers import generate_fields_user
from data import TestsUserData
import allure


class TestSendFormForgotPassword:
    @allure.title('Переход на форму восстановления пароля')
    def test_go_to_page_forgot_password_success(self, driver):
        page_forgot_password = PageForgotPassword(driver)
        page_forgot_password.go_to_form_login()
        page_forgot_password.go_to_page_forgot_password()

        assert page_forgot_password.get_current_url() == PageUrl.FORGOT_PASSWORD

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_click_button_forgot_password_success(self, driver):
        page_forgot_password = PageForgotPassword(driver)
        prepare_data = generate_fields_user(TestsUserData.FULL_DICTIONARY_FIELDS)
        page_forgot_password.go_to_form_login()
        page_forgot_password.go_to_page_forgot_password()
        page_forgot_password.complete_field_email(prepare_data['email'])
        page_forgot_password.go_to_page_reset_password()

        assert page_forgot_password.get_current_url() == PageUrl.RESET_PASSWORD


    @allure.title('Клик по кнопке показать/скрыть пароль')
    def test_button_ice_show_password_success(self, driver):
        page_forgot_password = PageForgotPassword(driver)
        prepare_data = generate_fields_user(TestsUserData.FULL_DICTIONARY_FIELDS)
        page_forgot_password.go_to_form_login()
        page_forgot_password.go_to_page_forgot_password()
        page_forgot_password.complete_field_email(prepare_data['email'])
        page_forgot_password.go_to_page_reset_password()

        assert page_forgot_password.check_button_show_password(prepare_data['password']) == True
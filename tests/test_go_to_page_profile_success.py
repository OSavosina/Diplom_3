from page_object.page_profile import PageProfile
from constants import PageUrl, UserFieldsCollection
from confest import driver, fixture_create_user
import allure


class TestPageProfile:
    @allure.title('Переход на страницу профиля для неавторизованного юзера')
    def test_go_to_page_profile_for_no_authorise_user(self, driver):
        page_profile = PageProfile(driver)
        page_profile.go_to_form_login()

        assert page_profile.get_current_url() == PageUrl.FORM_LOGIN


    @allure.title('Переход на страницу профиля для авторизованного юзера')
    def test_go_to_page_profile_for_authorise_user_success(self, driver, fixture_create_user):
        prepare_data = fixture_create_user

        page_profile = PageProfile(driver)
        page_profile.go_to_form_login()
        page_profile.send_form_login({UserFieldsCollection.EMAIL: prepare_data[f'{UserFieldsCollection.EMAIL}'], UserFieldsCollection.PASSWORD: prepare_data[f'{UserFieldsCollection.PASSWORD}']})
        page_profile.go_to_form_login()

        assert page_profile.get_current_url() == PageUrl.USER_PROFILE_PAGE


    @allure.title('Переход в раздел истории заказов')
    def test_go_to_page_profile_order_history_success(self, fixture_create_user, driver):
        prepare_data = fixture_create_user

        page_profile = PageProfile(driver)
        page_profile.go_to_form_login()
        page_profile.send_form_login({UserFieldsCollection.EMAIL: prepare_data[f'{UserFieldsCollection.EMAIL}'],
                                      UserFieldsCollection.PASSWORD: prepare_data[f'{UserFieldsCollection.PASSWORD}']})
        page_profile.go_to_form_login()
        page_profile.go_to_orders_history()

        assert page_profile.get_current_url() == PageUrl.ORDER_HISTORY


    @allure.title('Выход из аккаунта')
    def test_logout_success(self, driver, fixture_create_user):
        prepare_data = fixture_create_user

        page_profile = PageProfile(driver)
        page_profile.go_to_form_login()
        page_profile.send_form_login({UserFieldsCollection.EMAIL: prepare_data[f'{UserFieldsCollection.EMAIL}'],
                                      UserFieldsCollection.PASSWORD: prepare_data[f'{UserFieldsCollection.PASSWORD}']})
        page_profile.go_to_form_login()
        page_profile.logout()

        assert page_profile.get_current_url() == PageUrl.FORM_LOGIN
from page_object.order_page import PageOrder
from constants import PageUrl, UserFieldsCollection
import allure


class TestPageOrder:
    @allure.title('Переход на форму восстановления пароля')
    def test_go_to_constructor_success(self, driver):
        page_order = PageOrder(driver)
        page_order.go_to_constructor()

        assert page_order.get_current_url() == PageUrl.CONSTRUCTOR_PAGE


    @allure.title('Переход на ленту заказов')
    def test_go_to_feed_success(self, driver):
        page_order = PageOrder(driver)
        page_order.go_to_feed()

        assert page_order.get_current_url() == PageUrl.FEED_PAGE


    @allure.title('Открытие попап окна с деталями ингредиента')
    def test_open_ingredient_popup_success(self, driver):
        page_order = PageOrder(driver)

        assert page_order.open_popup_ingredient_details() == True


    @allure.title('Закрытие попап окна с деталями ингредиента')
    def test_close_ingredient_popup_success(self, driver):
        page_order = PageOrder(driver)
        page_order.open_popup_ingredient_details()

        assert page_order.close_popup_ingredient_details() == False


    @allure.title('При перемещении ингредиента в заказ, каунтер увеличивается')
    def test_drag_and_drop_ingredient_to_order_success(self, driver):
        page_order = PageOrder(driver)

        assert page_order.drag_and_drop_ingredients_to_order(driver) == True


    @allure.title('Кнопка оформления заказа открыта для авторизованных пользователей')
    def test_show_order_button_success(self, driver, fixture_create_user):
        prepare_data = fixture_create_user

        page_order = PageOrder(driver)
        page_order.go_to_form_login()
        page_order.send_form_login({UserFieldsCollection.EMAIL: prepare_data[f'{UserFieldsCollection.EMAIL}'], UserFieldsCollection.PASSWORD: prepare_data[f'{UserFieldsCollection.PASSWORD}']})

        assert page_order.find_button_order()





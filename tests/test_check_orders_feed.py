from page_object.feed_page import PageFeed
from constants import UserFieldsCollection
import allure


class TestOrdersFeed:
    @allure.title('Открытие попап окна по клику на заказ в ленте заказов')
    def test_open_order_popup_success(self, driver):
        page_feed = PageFeed(driver)
        page_feed.go_to_feed()
        page_feed.click_order_element()

        assert page_feed.open_popup_order_element() == True


    @allure.title('Заказ из истории заказов отображается в ленте заказов')
    def test_find_order_from_history_in_feed_orders_success(self, fixture_make_order, driver):
        made_order = fixture_make_order
        user_data = made_order['user_data']
        order_number = made_order['message']['order']['number']
        locator_order_number = f'//p[contains(text(), "#0{order_number}")]'

        page_feed = PageFeed(driver)
        page_feed.go_to_form_login()
        page_feed.send_form_login({UserFieldsCollection.EMAIL: user_data[f'{UserFieldsCollection.EMAIL}'],UserFieldsCollection.PASSWORD: user_data[f'{UserFieldsCollection.PASSWORD}']})
        page_feed.go_to_form_login()

        page_feed.go_to_tab_orders_history()
        order_from_history = page_feed.find_order_element(locator_order_number)

        page_feed.go_to_feed()
        order_from_feed = page_feed.find_order_element(locator_order_number)

        assert order_from_history == True and order_from_feed == True


    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_change_counter_for_all_time_success(self, fixture_make_order, driver):
        prepare_data = fixture_make_order

        page_feed = PageFeed(driver)
        page_feed.go_to_feed()
        save_order_count_start = page_feed.get_all_order_count()

        page_feed.create_order(prepare_data)

        page_feed.go_to_feed()
        save_order_count_end = page_feed.get_all_order_count()

        assert int(save_order_count_start) < int(save_order_count_end)


    @allure.title('При создании нового заказа счётчик Выполнено за сегодня')
    def test_change_counter_orders_for_today_success(self, fixture_make_order, driver):
        prepare_data = fixture_make_order

        page_feed = PageFeed(driver)
        page_feed.go_to_feed()
        save_order_count_start = page_feed.get_today_order_count()

        page_feed.create_order(prepare_data)

        page_feed.go_to_feed()
        save_order_count_end = page_feed.get_today_order_count()

        assert int(save_order_count_start) < int(save_order_count_end)


    @allure.title('Проверка отображения номера заказа в рабочем списке')
    def test_check_number_order_in_work_list_success(self, fixture_make_order, driver):
        page_feed = PageFeed(driver)
        page_feed.go_to_feed()

        assert page_feed.get_number_order_in_work_list() == True



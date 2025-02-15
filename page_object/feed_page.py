from page_object.base_page import BasePage
from locators import Locators
from constants import UserFieldsCollection
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from client.services import service_get_ingredients, service_create_order
import allure


class PageFeed(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход на форму авторизации')
    def go_to_form_login(self):
        self.find_element_base(locator=Locators.locator_button_user_profile, time=2).click()
        return self.get_current_url()

    @allure.step('Заполнение формы логина')
    def send_form_login(self, data):
        self.find_element_base(locator=Locators.locator_form_login_field_email, time=2).send_keys(
            data[UserFieldsCollection.EMAIL])
        self.find_element_base(locator=Locators.locator_form_login_field_password, time=2).send_keys(
            data[UserFieldsCollection.PASSWORD])
        self.find_element_base(locator=Locators.locator_form_login_button_enter, time=2).click()
        self.find_element_base(locator=Locators.locator_button_user_profile, time=2).is_displayed()



    @allure.step('Переход в раздел история заказов')
    def go_to_tab_orders_history(self):
        self.find_element_base(locator=Locators.locator_link_order_history, time=2).click()

    @allure.step('Поиск заказа в истории заказов')
    def find_order_element(self, locator):
        return self.find_element_base(locator=(By.XPATH, locator), time=2).is_displayed()



    @allure.step('Переход по клику на «Лента заказов»')
    def go_to_feed(self):
        self.find_element_base(locator=Locators.locator_link_feed, time=2).click()

    @allure.step('Получение текущего количества заказов за все время')
    def get_all_order_count(self):
        return self.find_element_base(locator=Locators.locator_counter_all_time, time=2).text

    @allure.step('Получение текущего количества заказов за сегодня')
    def get_today_order_count(self):
        return self.find_element_base(locator=Locators.locator_counter_today, time=2).text

    @allure.step('Поиск номера заказа в списке заказов в работе')
    def get_number_order_in_work_list(self):
        return self.find_element_base(locator=Locators.locator_order_in_work, time=2).is_displayed()



    @allure.step('Клик по элементу с заказом')
    def click_order_element(self):
        self.find_element_base(locator=Locators.locator_order_element, time=2).click()

    @allure.step('Окно с деталями заказа открыто')
    def open_popup_order_element(self):
        return self.find_element_base(locator=Locators.locator_popup_order_details, time=2).is_displayed()

    @allure.step('Закрыть окно с деталями заказа')
    def close_popup_order_element(self):
        self.find_element_base(locator=Locators.locator_popup_order_details, time=2).is_displayed()
        self.find_element_base(locator=Locators.locator_order_title, time=2).is_displayed()
        self.find_element_base(locator=Locators.locator_button_close_popup_order_details, time=2).click()



    @allure.step('Конструктор заказа')
    def drag_and_drop_ingredients_to_order(self, driver):
        draggable = self.find_element_base(locator=Locators.locator_link_burger, time=2)
        droppable = self.find_element_base(locator=Locators.locator_section_order, time=2)
        ActionChains(driver).drag_and_drop(draggable, droppable).perform()

    @allure.step('Создание заказа')
    def create_order(self, prepare_data):
        token = prepare_data['token']
        response_ingredients = service_get_ingredients()
        ingredient = response_ingredients.json()['data'][0]['_id']
        service_create_order({'ingredients': [ingredient]}, {'auth_key': token})

    @allure.step('Клик по кнопке Оформить заказ')
    def click_button_make_order(self):
        self.find_element_base(locator=Locators.locator_order_button, time=2).is_displayed()
        self.find_element_base(locator=Locators.locator_order_button, time=2).click()
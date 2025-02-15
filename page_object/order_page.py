from page_object.base_page import BasePage
from locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
from constants import UserFieldsCollection
import allure


class PageOrder(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход на форму авторизации')
    def go_to_form_login(self):
        self.find_element_base(locator=Locators.locator_button_user_profile, time=2).click()
        return self.get_current_url()

    @allure.step('Переход по клику на «Конструктор»')
    def go_to_constructor(self):
        self.find_element_base(locator=Locators.locator_link_constructor, time=2).click()

    @allure.step('Переход по клику на «Лента заказов»')
    def go_to_feed(self):
        self.find_element_base(locator=Locators.locator_link_feed, time=2).click()

    @allure.step('Клик по табу с начинками')
    def click_tab_ingredients(self):
        self.find_element_base(locator=Locators.locator_tab_ingredient, time=2).click()

    @allure.step('Клик по элементу списка с начинками')
    def click_element_list_ingredients(self):
        self.find_element_base(locator=Locators.locator_link_ingredient, time=2).click()


    @allure.step('Появление всплывающего окна с деталями ингредиента')
    def open_popup_ingredient_details(self):
        self.click_tab_ingredients()
        self.find_element_base(locator=Locators.locator_link_ingredient, time=2).is_displayed()
        self.click_element_list_ingredients()
        return self.find_element_base(locator=Locators.locator_popup_ingredient_details, time=2).is_displayed()

    @allure.step('Закрытие всплывающего окна с деталями ингредиента')
    def close_popup_ingredient_details(self):
        self.find_element_base(locator=Locators.locator_popup_ingredient_details, time=2).is_displayed()
        self.find_element_base(locator=Locators.locator_button_close_popup_ingredient_details, time=2).click()
        return self.find_element_base(locator=Locators.locator_popup_ingredient_details, time=2).is_displayed()

    @allure.step('Увеличить значение каунтера ингредиента при добавлении его в заказ')
    def drag_and_drop_ingredients_to_order(self, driver):
        self.click_tab_ingredients()

        draggable = self.find_element_base(locator=Locators.locator_link_ingredient, time=2)
        droppable = self.find_element_base(locator=Locators.locator_section_order, time=2)
        ActionChains(driver).drag_and_drop(draggable, droppable).perform()
        self.find_element_base(locator=Locators.locator_ingredient_counter, time=2).is_displayed()

        return self.find_element_base(locator=Locators.locator_ingredient_counter, time=2).text == '1'

    @allure.step('Найти кнопку оформления заказа')
    def find_button_order(self):
        return self.find_element_base(locator=Locators.locator_link_ingredient, time=2).is_displayed()

    @allure.step('Заполнение формы логина')
    def send_form_login(self, data):
        self.find_element_base(locator=Locators.locator_form_login_field_email, time=2).send_keys(data[UserFieldsCollection.EMAIL])
        self.find_element_base(locator=Locators.locator_form_login_field_password, time=2).send_keys(data[UserFieldsCollection.PASSWORD])
        self.find_element_base(locator=Locators.locator_form_login_button_enter, time=2).click()
        self.find_element_base(locator=Locators.locator_button_user_profile, time=2).is_displayed()







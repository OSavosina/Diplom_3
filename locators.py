from selenium.webdriver.common.by import By

class Locators:
    locator_button_user_profile = (By.XPATH, '//p[contains(@class, "AppHeader_header__linkText__3q_va") and text() = "Личный Кабинет"]')

    locator_link_forgot_password = (By.XPATH, '//a[@href="/forgot-password"]')
    locator_field_email = (By.XPATH, '//input[@class="text input__textfield text_type_main-default"]')
    locator_button_forgot_password = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    locator_field_type_password = (By.XPATH, '//input[contains(@class, "text input__textfield text_type_main-default") and @type="password"]')
    locator_field_type_text = (By.XPATH, '//input[contains(@class, "text input__textfield text_type_main-default") and @type="text" and @name="Введите новый пароль"]')
    locator_icon_show_password = (By.XPATH, '//div[@class="input__icon input__icon-action"]/child::*/child::*')

    locator_form_login_field_email = (By.XPATH, '//label/following::input[@name="name"]')
    locator_form_login_field_password = (By.XPATH, '//label/following::input[@name="Пароль"]')
    locator_form_login_button_enter = (By.XPATH, "//button[contains(text(), 'Войти')]")
    locator_form_login_button_exit = (By.XPATH, "//button[contains(text(), 'Выход')]")
    locator_form_login_title_exit = (By.XPATH, "//h2[contains(text(), 'Вход')]")
    locator_link_order_history = (By.XPATH, '//a[@href="/account/order-history"]')

    locator_link_constructor = (By.XPATH, "//p[contains(text(), 'Конструктор')]/parent::a[1]")
    locator_link_feed = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]/parent::a[1]")


    locator_tab_ingredient = (By.XPATH, '//section[@class="BurgerIngredients_ingredients__1N8v2"]/child::div/div[3]')
    locator_section_order = (By.XPATH, '//section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]/ul')
    locator_popup_ingredient_details = (By.XPATH, '//div[@class="Modal_modal__contentBox__sCy8X pt-10 pb-15"]')
    locator_button_close_popup_ingredient_details = (By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    locator_link_ingredient = (By.XPATH, '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"]/child::a[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]')
    locator_link_burger = (By.XPATH, '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"]/child::a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')
    locator_order_title = (By.XPATH, '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    locator_ingredient_counter = (By.XPATH, '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"]/child::a[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]/child::div[@class="counter_counter__ZNLkj counter_default__28sqi"]/p')
    locator_order_button = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")


    locator_order_element = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']/child::a[@href='/feed/67afa5499ed280001b57406d']")
    locator_popup_order_details = (By.XPATH, '//div[@class="Modal_modal__contentBox__sCy8X pt-30 pb-30"]')
    locator_button_close_popup_order_details = (By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')

    locator_counter_all_time = (By.XPATH, '//div[@class="undefined mb-15"]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    locator_counter_today = (By.XPATH, '//p[contains(text(), "Выполнено за сегодня")]/following::p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')

    locator_order_in_work = (By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/child::li[@class="text text_type_digits-default mb-2"]')




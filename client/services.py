from client.api import post_api, delete_api, get_api
from constants import RoutesName
import allure


@allure.step('Создание юзера')
def service_sign_up(data):
    return post_api(RoutesName.SIGN_UP_USER, data)

@allure.step('Удаление юзера')
def service_delete_user():
    return delete_api(RoutesName.DELETE_USER)

@allure.step('Авторизация юзера')
def service_sign_in(data):
    return post_api(RoutesName.SIGN_IN_USER, data)

@allure.step('Создание заказа')
def service_create_order(data, headers_dict):
    prepare_headers = {'Authorization': headers_dict['auth_key']}
    return post_api(RoutesName.CREATE_ORDER, data, prepare_headers)

@allure.step('Получение списка ингредиентов')
def service_get_ingredients():
    return get_api(RoutesName.INGREDIENTS)
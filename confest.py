import pytest
from selenium import webdriver
from helpers.helpers import generate_fields_user
from client.services import service_sign_up, service_delete_user, service_get_ingredients, service_create_order
from data import TestsUserData
from constants import PageUrl

base_url = PageUrl.MAIN_PAGE

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
    else:
        raise ValueError('Unknown browser type')
    browser.get(base_url)
    yield browser
    browser.quit()

@pytest.fixture
def fixture_create_user():
    prepare_data = generate_fields_user(TestsUserData.FULL_DICTIONARY_FIELDS)
    service_sign_up(prepare_data)
    yield prepare_data
    service_delete_user()

@pytest.fixture
def fixture_make_order():
    prepare_data = generate_fields_user(TestsUserData.FULL_DICTIONARY_FIELDS)
    response_auth = service_sign_up(prepare_data)
    token = response_auth.json()['accessToken']

    response_ingredients = service_get_ingredients()
    ingredient = response_ingredients.json()['data'][0]['_id']

    response = service_create_order({'ingredients': [ingredient]}, {'auth_key': token})
    message = response.json()

    yield {'message': message, 'user_data': prepare_data, 'token': token}
    service_delete_user()
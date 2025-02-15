class PageUrl:
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site'
    CONSTRUCTOR_PAGE = f"{MAIN_PAGE+'/'}"
    FEED_PAGE = f"{MAIN_PAGE+'/feed'}"
    FORGOT_PASSWORD = f'{MAIN_PAGE}/forgot-password'
    RESET_PASSWORD = f'{MAIN_PAGE}/reset-password'
    FORM_LOGIN = f'{MAIN_PAGE}/login'
    USER_PROFILE_PAGE = f"{MAIN_PAGE + '/account'}"
    ORDER_HISTORY = f"{MAIN_PAGE + '/account/order-history'}"


class UserFieldsCollection:
    EMAIL = 'email'
    PASSWORD = 'password'
    NAME = 'name'

class HostName:
    HOST_NAME = 'https://stellarburgers.nomoreparties.site/api'

class RoutesName:
    SIGN_UP_USER = '/auth/register'
    DELETE_USER = '/auth/user'
    SIGN_IN_USER = '/auth/login'
    INGREDIENTS = '/ingredients'
    CREATE_ORDER = '/orders'
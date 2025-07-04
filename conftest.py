import pytest
from DrissionPage import ChromiumPage
from pages.login_page import LoginPage
from config.config import get_config_item

@pytest.fixture(scope='session')
def page():
    page = ChromiumPage()
    yield page
    page.quit()

# 登录后页面fixture
@pytest.fixture(scope='function')
def login_page(page, request):
    # 如果用例标记了 no_login，则不自动登录
    if 'no_login' in request.keywords:
        return page
    login = LoginPage(page)
    login.login()  # 使用配置文件中的账号
    return page 
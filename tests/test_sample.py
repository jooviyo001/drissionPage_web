import allure
import pytest
from config.config import get_config_item

# 需要登录的用例
@allure.feature('需要登录的页面')
def test_login_required(login_page):
    with allure.step('访问需要登录的页面'):
        base_url = get_config_item('base_url')
        login_page.get(f'{base_url}/user')
    with allure.step('断言已登录'):
        assert '用户中心' in login_page.html  # 替换为实际断言

# 不需要登录的用例
@pytest.mark.no_login
@allure.feature('无需登录的页面')
def test_baidu_search(page):
    with allure.step('打开百度首页'):
        page.get('https://www.baidu.com')
    with allure.step('输入搜索内容'):
        page.ele('id=kw').input('DrissionPage')
    with allure.step('点击搜索按钮'):
        page.ele('id=su').click()
    with allure.step('断言结果页包含关键词'):
        assert 'DrissionPage' in page.html 
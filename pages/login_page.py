from pages.base_page import BasePage
from config.config import get_config_item

class LoginPage(BasePage):
    def login(self, username=None, password=None):
        # 使用配置文件中的登录URL
        login_url = get_config_item('login_url')
        self.page.get(login_url)
        
        # 使用配置文件中的账号，或传入的参数
        username = username or get_config_item('username')
        password = password or get_config_item('password')
        
        self.input('id=username', username)
        self.input('id=password', password)
        self.click('id=loginBtn') 
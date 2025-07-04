import time
from utils.logger import get_logger

class BasePage:
    def __init__(self, page):
        self.page = page
        self.logger = get_logger()

    def find(self, locator):
        """查找单个元素"""
        return self.page.ele(locator)

    def finds(self, locator):
        """查找多个元素"""
        return self.page.eles(locator)

    def input(self, locator, value):
        """输入内容"""
        ele = self.find(locator)
        ele.input(value)
        return ele

    def click(self, locator):
        """点击元素"""
        ele = self.find(locator)
        ele.click()
        return ele

    def text(self, locator):
        """获取元素文本"""
        ele = self.find(locator)
        return ele.text

    # 页面导航操作
    def get(self, url):
        """访问页面"""
        self.logger.info(f"访问页面: {url}")
        return self.page.get(url)

    def back(self):
        """后退"""
        self.logger.info("页面后退")
        return self.page.back()

    def forward(self):
        """前进"""
        self.logger.info("页面前进")
        return self.page.forward()

    def refresh(self):
        """刷新页面"""
        self.logger.info("刷新页面")
        return self.page.refresh()

    def get_url(self):
        """获取当前URL"""
        return self.page.url

    def get_title(self):
        """获取页面标题"""
        return self.page.title

    # 元素等待操作
    def wait_ele(self, locator, timeout=10):
        """等待元素出现"""
        self.logger.info(f"等待元素: {locator}")
        return self.page.wait.ele(locator, timeout=timeout)

    def wait_ele_disappear(self, locator, timeout=10):
        """等待元素消失"""
        self.logger.info(f"等待元素消失: {locator}")
        return self.page.wait.ele_disappear(locator, timeout=timeout)

    def wait_clickable(self, locator, timeout=10):
        """等待元素可点击"""
        self.logger.info(f"等待元素可点击: {locator}")
        return self.page.wait.ele_clickable(locator, timeout=timeout)

    def wait_visible(self, locator, timeout=10):
        """等待元素可见"""
        self.logger.info(f"等待元素可见: {locator}")
        return self.page.wait.ele_visible(locator, timeout=timeout)

    # 窗口操作
    def switch_to_window(self, index=1):
        """切换到指定窗口"""
        self.logger.info(f"切换到窗口: {index}")
        return self.page.change_window(index)

    def close_window(self):
        """关闭当前窗口"""
        self.logger.info("关闭当前窗口")
        return self.page.close_window()

    def get_window_handles(self):
        """获取所有窗口句柄"""
        return self.page.windows

    # 截图操作
    def screenshot(self, path=None):
        """截图"""
        if not path:
            path = f"screenshots/screenshot_{int(time.time())}.png"
        self.logger.info(f"截图保存到: {path}")
        return self.page.save_screenshot(path)

    def screenshot_element(self, locator, path=None):
        """元素截图"""
        if not path:
            path = f"screenshots/element_{int(time.time())}.png"
        ele = self.find(locator)
        self.logger.info(f"元素截图保存到: {path}")
        return ele.save_screenshot(path)

    # 滚动操作
    def scroll_to_element(self, locator):
        """滚动到元素"""
        ele = self.find(locator)
        self.logger.info(f"滚动到元素: {locator}")
        return ele.scroll.to_element()

    def scroll_to_bottom(self):
        """滚动到底部"""
        self.logger.info("滚动到页面底部")
        return self.page.scroll.to_bottom()

    def scroll_to_top(self):
        """滚动到顶部"""
        self.logger.info("滚动到页面顶部")
        return self.page.scroll.to_top()

    # 鼠标操作
    def hover(self, locator):
        """鼠标悬停"""
        ele = self.find(locator)
        self.logger.info(f"鼠标悬停: {locator}")
        return ele.hover()

    def right_click(self, locator):
        """右键点击"""
        ele = self.find(locator)
        self.logger.info(f"右键点击: {locator}")
        return ele.right_click()

    def double_click(self, locator):
        """双击"""
        ele = self.find(locator)
        self.logger.info(f"双击: {locator}")
        return ele.double_click()

    # 键盘操作
    def press_key(self, key):
        """按键"""
        self.logger.info(f"按键: {key}")
        return self.page.key.press(key)

    def input_keys(self, keys):
        """输入按键序列"""
        self.logger.info(f"输入按键: {keys}")
        return self.page.key.input(keys)

    # 表单操作
    def select_option(self, locator, value):
        """选择下拉选项"""
        ele = self.find(locator)
        self.logger.info(f"选择选项: {value}")
        return ele.select(value)

    def clear_input(self, locator):
        """清空输入框"""
        ele = self.find(locator)
        self.logger.info(f"清空输入框: {locator}")
        return ele.clear()

    # 属性操作
    def get_attribute(self, locator, attribute):
        """获取元素属性"""
        ele = self.find(locator)
        return ele.attr(attribute)

    def set_attribute(self, locator, attribute, value):
        """设置元素属性"""
        ele = self.find(locator)
        return ele.set_attr(attribute, value)

    # 页面状态检查
    def is_element_exist(self, locator):
        """检查元素是否存在"""
        return self.page.ele(locator, timeout=0) is not None

    def is_element_visible(self, locator):
        """检查元素是否可见"""
        ele = self.page.ele(locator, timeout=0)
        return ele and ele.states.is_displayed

    def is_element_enabled(self, locator):
        """检查元素是否可用"""
        ele = self.page.ele(locator, timeout=0)
        return ele and ele.states.is_enabled

    # 页面加载等待
    def wait_page_load(self, timeout=30):
        """等待页面加载完成"""
        self.logger.info("等待页面加载完成")
        return self.page.wait.load_complete(timeout=timeout)

    def wait_ajax_complete(self, timeout=10):
        """等待AJAX请求完成"""
        self.logger.info("等待AJAX请求完成")
        return self.page.wait.ajax_complete(timeout=timeout) 
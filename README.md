# DrissionPage + Pytest + Allure 自动化测试框架

## 浏览器操作方法

BasePage 提供了丰富的浏览器操作方法：

### 页面导航

- `get(url)`: 访问页面
- `back()`: 后退
- `forward()`: 前进  
- `refresh()`: 刷新
- `get_url()`: 获取当前URL
- `get_title()`: 获取页面标题

### 元素等待

- `wait_ele(locator, timeout)`: 等待元素出现
- `wait_ele_disappear(locator, timeout)`: 等待元素消失
- `wait_clickable(locator, timeout)`: 等待元素可点击
- `wait_visible(locator, timeout)`: 等待元素可见

### 窗口操作

- `switch_to_window(index)`: 切换窗口
- `close_window()`: 关闭当前窗口
- `get_window_handles()`: 获取所有窗口句柄

### 截图操作

- `screenshot(path)`: 页面截图
- `screenshot_element(locator, path)`: 元素截图

### 滚动操作

- `scroll_to_element(locator)`: 滚动到元素
- `scroll_to_bottom()`: 滚动到底部
- `scroll_to_top()`: 滚动到顶部

### 鼠标操作

- `hover(locator)`: 鼠标悬停
- `right_click(locator)`: 右键点击
- `double_click(locator)`: 双击

### 键盘操作

- `press_key(key)`: 按键
- `input_keys(keys)`: 输入按键序列

### 表单操作

- `select_option(locator, value)`: 选择下拉选项
- `clear_input(locator)`: 清空输入框

### 属性操作

- `get_attribute(locator, attribute)`: 获取元素属性
- `set_attribute(locator, attribute, value)`: 设置元素属性

### 页面状态检查

- `is_element_exist(locator)`: 检查元素是否存在
- `is_element_visible(locator)`: 检查元素是否可见
- `is_element_enabled(locator)`: 检查元素是否可用

### 页面加载等待

- `wait_page_load(timeout)`: 等待页面加载完成
- `wait_ajax_complete(timeout)`: 等待AJAX请求完成

## 环境配置

支持多环境切换，支持以下环境：

- dev: 开发环境
- test: 测试环境  
- prod: 生产环境

### 切换环境的方法

#### 1. 推荐：设置环境变量（适用于本地和Jenkins）

```bash
# Windows PowerShell
$env:TEST_ENV="test"; pytest

# Windows CMD
set TEST_ENV=test && pytest

# Linux/Mac
TEST_ENV=test pytest
```

#### 2. 直接修改配置文件（不推荐，适合本地临时调试）

编辑 `config/config.py` 文件，修改 ENV 默认值：

```python
ENV = 'test'  # 改为 'dev', 'test', 或 'prod'
```

#### 3. 查看当前环境

```python
from config.config import print_env_info
print_env_info()
```

### Jenkinsfile 环境切换示例

```groovy
pipeline {
    agent any
    environment {
        TEST_ENV = 'test' // 这里切换环境
    }
    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest --alluredir=allure-results'
            }
        }
        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
        }
    }
}
```

## 日志模块

日志文件默认输出在 logs/test.log，控制台和文件均有日志。

使用方法：

```python
from utils.logger import get_logger
logger = get_logger()
logger.info('信息日志')
logger.error('错误日志')
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行测试

```bash
pytest --alluredir=allure-results
```

## 生成 Allure 报告

```bash
allure serve allure-results
```

## 目录结构

```plaintext
drissionPage_web/
├── config/
│   └── config.py
├── utils/
│   └── logger.py
├── requirements.txt
├── pytest.ini
├── conftest.py
├── Jenkinsfile
├── README.md
├── tests/
│   └── test_sample.py
├── pages/
│   └── base_page.py
```

## Jenkins 集成

- 参考 Jenkinsfile，需安装 Allure 插件。
- 支持流水线自动执行测试并生成报告。

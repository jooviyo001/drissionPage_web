import os

# 环境配置
# 切换环境：
# 1. 推荐：设置环境变量 TEST_ENV（如 Jenkinsfile 或命令行中）
# 2. 未设置时，使用下方 ENV 默认值
ENV = os.getenv('TEST_ENV', 'test')  # 默认环境为'test'

# 不同环境的配置
CONFIG = {
    'dev': {
        'base_url': 'https://dev.example.com',
        'login_url': 'https://dev.example.com/login',
        'username': 'dev_user',
        'password': 'dev_pass',
        'timeout': 10,
        'headless': False
    },
    'test': {
        'base_url': 'http://192.168.20.102/',
        'login_url': 'http://192.168.20.102/login',
        'username': '13721455568',
        'password': '123456',
        'timeout': 15,
        'headless': True
    },
    'prod': {
        'base_url': 'https://www.example.com',
        'login_url': 'https://www.example.com/login',
        'username': 'prod_user',
        'password': 'prod_pass',
        'timeout': 20,
        'headless': True
    }
}

# 获取当前环境配置
def get_config():
    return CONFIG.get(ENV, CONFIG[ENV])

# 获取配置项
def get_config_item(key):
    return get_config().get(key)

# 获取当前环境名称
def get_current_env():
    return ENV

# 打印当前环境信息
def print_env_info():
    config = get_config()
    print(f"当前环境: {ENV}")
    print(f"基础URL: {config.get('base_url')}")
    print(f"超时时间: {config.get('timeout')}秒")
    print(f"无头模式: {config.get('headless')}")

# 切换环境函数
def switch_env(env_name):
    """切换环境"""
    global ENV
    if env_name not in CONFIG:
        print(f"错误: 不支持的环境 '{env_name}'")
        print(f"支持的环境: {list(CONFIG.keys())}")
        return False
    
    ENV = env_name
    print(f"环境已切换到: {env_name}")
    print_env_info()
    # return True 

if __name__ == "__main__":
    # print(get_config())
    print(get_config_item('base_url'))
    # print_env_info()
    # switch_env('test')
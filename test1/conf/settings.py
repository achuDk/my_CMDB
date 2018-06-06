#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

# 定义项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 定义工作模式
MODE = 'Agent'
# MODE = 'SSH'
# MODE = 'Salt'

# 定义是否开启测试模式
TEST_MODE = True

# SSH模式连接所需配置
SSH_PORT = 22
SSH_USERNAME = 'root'
SSH_PWD = '123456'


# 定义启用的插件
PLUGINS = {

}
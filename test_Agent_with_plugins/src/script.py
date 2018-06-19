#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Agent模式共两步：
    1. 获取本机的各种信息
    2. 将信息发送至API
"""

from test_Agent_with_plugins.conf import settings

data_info = {}
class AgentClient():
    def __init__(self):
        self.hostname = self.shell_cmd('hostname')
        data_info['hostname'] = self.hostname

    #
    def run(self):
        # 获取各服务器信息
        data_info = self.get_server_info()
        # 将获取的信息发送至API并返回状态
        response = self.send_server_info(data_info)
        return response

    # 获取各服务器信息
    def get_server_info(self):
        data_info['disk'] = Disk_info().linux()
        data_info['mem'] = Mem_info().linux()
        print('----->  data_info：',data_info)
        return data_info

    # 将获取的信息发送至API并返回状态
    def send_server_info(self,data_info):
        import requests
        # response = requests.post(settings.API,data=data_info)
        print('settings.API :',settings.API)
        print('data_info : ',data_info)
        response = 'ok'
        # response = 'error'
        return response

    def shell_cmd(self,cmd):
        import subprocess
        ret = subprocess.getoutput(cmd)
        print(cmd,'命令执行结果：',ret)
        return ret

class Disk_info(AgentClient):
    def linux(self):
        return self.shell_cmd('echo disk_info')

class Mem_info(AgentClient):
    def linux(self):
        return self.shell_cmd('echo mem_info')
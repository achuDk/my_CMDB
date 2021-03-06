#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Agent模式共两步：
    1. 获取本机的各种信息
    2. 将信息发送至API
"""

from test_Agent_Basic.conf import settings

data_info = {}
class Agent():
    def __init__(self):
        self.hostname = self.shell_cmd('hostname')
        data_info['hostname'] = self.hostname


    def get_server_info(self):
        data_info['disk'] = self.disk_info()
        data_info['mem'] = self.mem_info()
        print('----->  data_info：',data_info)
        return data_info

    def send_server_info(self):
        data_info = self.get_server_info()
        import requests
        # response = requests.post(settings.API,data=data_info)
        # response = 'ok'
        response = 'error'
        return response

    def run(self):
        response = self.send_server_info()
        return response


    def shell_cmd(self,cmd):
        import subprocess
        ret = subprocess.getoutput(cmd)
        print(cmd,'命令执行结果：',ret)
        return ret

    def disk_info(self):
        # ret = self.shell_cmd('df -h')
        ret = self.shell_cmd('echo disk_info')
        return ret

    def mem_info(self):
        # ret = self.shell_cmd('free -m')
        ret = self.shell_cmd('echo mem_info')
        return ret


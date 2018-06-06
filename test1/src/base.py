#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
from test1.conf import settings

mode_list = ['Agent', 'SSH', 'Salt']
class BasePlugin():
    def __init__(self,hostname=''):
        self.test_mode = settings.TEST_MODE
        self.hostname = hostname
        if hasattr(settings, 'MODE'):
            self.mode = settings.MODE
        else:
            self.mode = 'Agent'

    def Agent(self,cmd):
        import subprocess
        output = subprocess.getoutput(cmd)
        return output

    def SSH(self,cmd):
        import paramiko
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname, port=settings.SSH_PORT, username=settings.SSH_USERNAME, password=settings.SSH_PWD)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        ssh.close()
        ret = stdout.read()
        return ret

    def Salt(self,cmd):
        from salt import salt.client
        local = salt.client.LocalClient()
        ret = local.cmd(self.hostname,'cmd.run',[cmd])
        return ret[self.hostname]


    def shell_cmd(self,cmd):
        if self.mode not in mode_list:
            raise Exception('程序工作模式错误')
        func = getattr(self,self.mode)
        ret = func(cmd)
        return ret

    def execute(self):
        return self.linux()

    def linux(self):
        raise Exception('请在派生来中自定义该方法')


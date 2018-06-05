#!/usr/bin/env python
# -*- coding:utf-8 -*-


#
class BaseCls():
    def post_asset(self):
        pass
    def process(self):
        """
        要求派生类必须自己重新实现该方法，否则报错
        :return:
        """
        raise NotImplementedError('You must redefine this method in your derive class!')

class SBaseCls(BaseCls):
    def send_asset(self):
        pass

class Agent(BaseCls):
    def process(self):
        # 1. 采集数据

        # 2. 发送数据至API
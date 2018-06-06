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
    def get_asset(self):
        pass

class Salt(SBaseCls):
    def process(self):
        return self.linux()

    def linux(self):
        pass
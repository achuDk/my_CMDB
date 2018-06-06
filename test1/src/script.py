#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
from test1.conf import settings


def run():
    if settings.MODE == 'Agent':
        client = ''
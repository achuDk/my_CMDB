#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests

host_data = {
    "status":True,
    "data":{
        "hostname":"host1",
        "disk":{"status":True,"data":'xxx'},
        "mem":{"status":True,"data":'xxx'},
        "nic":{"status":True,"data":'xxx'},
    },
    "key":"c9834yuh0mm02d89u509",
}


# requests.get(url='http://127.0.0.1:8080/api/asset/?k1=123&k2=0980')
# response = requests.get(url='http://127.0.0.1:8080/api/asset/',params={'k1':'v1','k2':'v2'})

# response = requests.post(
#     url = 'http://127.0.0.1:8080/api/asset/',
#     params={'k1':'v1','k2':'v2'},   #GET形式传值
#     data = host_data,               #POST形式传值
#     headers={'headers':'HHH'},      #请求头数据
# )
# print('response:',requests)


response = requests.post(
    url = 'http://127.0.0.1:8080/api/asset/',
    params={'k1':'v1','k2':'v2'},   #GET形式传值
    json=host_data,
    headers={'headers':'HHH'},      #请求头数据
)
print('response:',requests)
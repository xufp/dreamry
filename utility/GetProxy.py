# -*- coding: utf-8 -*-
'''
Created on 2017年12月10日

@author: spring8743
'''

import requests
from Config import *

def get_proxy():
    try:
        request = requests.get(proxy_url)
        proxy = request.content
        return proxy
    except Exception:
        print Exception.message


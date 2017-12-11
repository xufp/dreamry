# -*- coding: utf-8 -*-
'''
Created on 2017年12月10日

@author: spring8743
'''

from sqlobject import *
import datetime
from Config import uri

sqlhub.processConnection = connectionForURI(uri)

class VisitRecord(SQLObject):
    class sqlmeta:
        lazyUpdate = True

    country_code = StringCol(length=150, notNone=True)
    
    asin = StringCol(length=150, notNone=True)
    
    item_title = StringCol(length=2000, notNone=True)
    
    keyword = StringCol(length=500, notNone=True)
    
    keyword_type = StringCol(length=500, notNone=True)
    
    proxy_ip = StringCol(length=500, notNone=True)
    
    visit_count = IntCol(default = 0, notNone=True)
    
    add_cart_count = IntCol(default = 0, notNone=True)
    
    wish_list_count = IntCol(default = 0, notNone=True)
    
    search_date = DateCol(notNone=True)
    
    search_time = TimeCol(notNone=True)


def update_record(country_code, asin, item_title, keyword, keyword_type, proxy_ip, visit_count, add_cart_count, wish_list_count,search_date, search_time):
    newRow = VisitRecord(country_code = country_code, asin = asin, item_title = item_title, keyword = keyword, keyword_type = keyword_type, proxy_ip = proxy_ip, visit_count = visit_count, add_cart_count = add_cart_count, wish_list_count = wish_list_count, search_date = search_date, search_time = search_time)
    newRow.sync()  
    
    
      
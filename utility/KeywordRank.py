# -*- coding: utf-8 -*-
'''
Created on 2017年12月10日

@author: spring8743
'''

from sqlobject import *
import datetime
from Config import uri

sqlhub.processConnection = connectionForURI(uri)


class KeywordRank(SQLObject):
    
    class sqlmeta:
        lazyUpdate = True

    
#     id = StringCol(length=10, notNone=True)
    
    country_code = StringCol(length=150, notNone=True)
    
    asin = StringCol(length=150, notNone=True)
    
    item_title = StringCol(length=2000, notNone=True)
    
    keyword = StringCol(length=500, notNone=True)
    
    keyword_type = StringCol(length=500, notNone=True)
    
    rank_page = IntCol(default = 0, notNone=True)
    
    rank_rowid = IntCol(default = 0, notNone=True)
    
    search_date = DateCol(notNone=True)
    
    search_time = TimeCol(notNone=True)
    
    
def update_record(country_code, asin, item_title, keyword, keyword_type, page, rowid, search_date, search_time):
        obj = KeywordRank.selectBy(keyword=keyword, asin = asin, search_date = search_date)
        if list(obj).__len__() >= 1:
            # update record
            obj[0].set(country_code = country_code)
            obj[0].set(item_title = item_title)
            obj[0].set(keyword_type = keyword_type)
            obj[0].set(rank_page = page)
            obj[0].set(rank_rowid = rowid)
            obj[0].set(search_time = search_time)
            obj[0].sync() 
        else:
            # insert record
            newRow = KeywordRank(country_code = country_code, asin = asin, item_title = item_title, keyword = keyword, keyword_type = keyword_type, rank_page = page, rank_rowid = rowid, search_date = search_date, search_time = search_time)
            newRow.sync()    

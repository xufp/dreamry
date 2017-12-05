# -*- coding: utf-8 -*-
'''
Created on 2017年12月2日

@author: spring8743
'''

import MySQLdb
import sys

#infomation about mysql server
HOST = '127.0.0.1'
PORT = 3306
USER = 'root'
PASSWD = 'zaq12wsX'
DB = 'Amazon_DB'
CHARSET = 'utf8'

def get_connection():
    try:
        conn = MySQLdb.connect(host=HOST,port=PORT,user=USER,passwd=PASSWD,db=DB,charset=CHARSET)
        return conn
    except Exception,e:
        print 'error while connecting to mysql'
        sys.exit()
    


def update_record(table_name,country_code, asin, item_title, keyword, keyword_type, page, rowid, search_date, search_time):
    try:
        conn = get_connection()
        conn.autocommit(False)
        cursor = conn.cursor()
        SQL = 'select * from %s where asin="%s" and keyword="%s" and search_date="%s"'%(table_name, asin, keyword, search_date)
        cursor.execute(SQL)
        result = cursor.fetchall()
        if not result:
            SQL = 'insert into %s (country_code, asin, item_title, keyword, keyword_type, rank_page, rank_rowid, search_date, search_time) values("%s", "%s","%s", "%s", "%s", "%s", "%s", "%s", "%s");' %(table_name,country_code, asin, item_title, keyword, keyword_type, page, rowid, search_date, search_time)
#             print SQL
            cursor.execute(SQL)
        else:
            # update record
            SQL = 'update %s set country_code= "%s", item_title="%s", keyword_type="%s", rank_page=%s, rank_rowid=%s, search_time="%s"  where asin="%s" and keyword="%s" and search_date = "%s" ;'%(table_name, country_code, item_title, keyword_type, page, rowid, search_time, asin, keyword, search_date)
#             print SQL
            cursor.execute(SQL)
            
        conn.commit()
    except Exception, e:
        print e.message    
    finally:
        cursor.close()
        conn.close()
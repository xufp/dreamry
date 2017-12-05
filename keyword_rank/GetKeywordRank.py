# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-08-25 22:19:42
# @Last modified by:   LC
# @Last Modified time: 2016-09-02 22:09:13
# @Email: liangchaowu5@gmail.com

from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import time
from DBUtility import update_record

DOMAINS = {
    'CA':'ca',
    'DE':'de',
    'ES':'es',
    'FR':'fr',
    'IN':'in',
    'IT':'it',
    'JP':'co.jp',
    'UK':'co.uk',
    'US':'com'
    }

#the max page you want to find
max_page = 21

#Next Page Button
nextPage = '#pagnNextString'


def get_product_page(search_keywords, item_title, country_code, asin,driver):
    """find the page of an item described by item_keywords when searching with search_keywords
    
    Args:
        search_keywords (str): keywords to search items, joined by '+'
        item_keywords (str): words to describe an item, part of title of the item
    
    Returns:
    """
   
    found = False
    #Page is the page rank
    page = 0
    #Row id is the Item rank in the page
    rowid = 0
    try:
        target_url = 'https://www.amazon.%s/s/ref=sr_pg_%s?page=%s&keywords=%s&ie=UTF8'%(DOMAINS[country_code],1, 1, search_keywords.keys()[0])
        driver.get(target_url)

        #Loop the first 20 pages to find the product by keyword        
        for i in xrange(1, max_page):
            text = driver.page_source
            soup = BeautifulSoup(text, 'lxml')
            titles = soup.find_all('h2')
            
            #row id
            j = 0
            for title in titles:
                j = j + 1
                if item_title in title.get('data-attribute', ''):
#                     print 'Page %s: Found'%i
                    found = True
#                     print title.get('data-attribute')
                            
                    break
            if found:
                #If found the product, then set the page and row id
                page = i
                rowid = j
                break
            else:
#                 print 'Page %s: Not Found'%i
                #If not found, then click the next page and sleep 20 secs
                driver.find_element_by_css_selector(nextPage).click()
                time.sleep(20)
                
        update_record('keyword_rank',country_code, asin, item_title,search_keywords.keys()[0], search_keywords.values()[0], page, rowid, datetime.datetime.now().strftime('%Y-%m-%d'), datetime.datetime.now().strftime('%H:%M:%S'))
        return country_code, asin, item_title,search_keywords.keys()[0], search_keywords.values()[0], page, rowid, datetime.datetime.now().strftime('%Y-%m-%d'), datetime.datetime.now().strftime('%H:%M:%S')
            
    except Exception, e:
        print e.message
       
def get_product_page_by_list(search_keywords, item_title, country_code, asin):
    #chrome driver
    driver = webdriver.Chrome('/Users/spring8743/Documents/workspace/chromedriver')
    
    for keywords in search_keywords:
#         print keywords
        print get_product_page(keywords, item_title, country_code, asin,driver)
        time.sleep(20)
    
    driver.quit() 
    
     



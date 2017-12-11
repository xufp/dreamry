# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import time
from utility.Config import *
from utility.GetProxy import get_proxy
import random
from utility.VisitRecord import update_record


def search_product_page(search_keywords, item_title, country_code, asin):
    """find the page of an item described by item_keywords when searching with search_keywords
    
    Args:
        search_keywords (str): keywords to search items, joined by '+'
        item_keywords (str): words to describe an item, part of title of the item
    
    Returns:
    """
    #setup the proxy on Chrome
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--proxy-server=%s' % get_proxy())
#     driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    proxy_ip = get_proxy()
    
    # No proxy testing on Macbook
    driver = webdriver.Chrome(chrome_driver)
    
    visit_count = 0
    add_cart_count = 0
    wish_list_count = 0
   
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
                    found = True
                    #If find the product, then click the item
                    driver.find_element_by_link_text(item_title).click()
                    time.sleep(20)
                    
                    # If found the item by keword, then set the visit count = 1
                    visit_count = 1
                    
                    #Add to cart
                    if random.random()< possibility:
                        cart = '#add-to-cart-button'
                        try:
                            driver.find_element_by_css_selector(cart).click()
                            
                            #If click the add to cart button successuflly, then set the add cart count = 1
                            add_cart_count = 1
                            print '================successfully add to cart==================='
                            time.sleep(5)
                        except Exception,e:
                            print 'Error while adding item to cart\n%s'%e.message
                            return
                            
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
                
        update_record(country_code, asin, item_title,search_keywords.keys()[0], search_keywords.values()[0], proxy_ip, visit_count, add_cart_count, wish_list_count,datetime.datetime.now().strftime('%Y-%m-%d'), datetime.datetime.now().strftime('%H:%M:%S'))
        driver.quit() 
        return country_code, asin, item_title,search_keywords.keys()[0], search_keywords.values()[0], proxy_ip, visit_count, add_cart_count, wish_list_count,datetime.datetime.now().strftime('%Y-%m-%d'), datetime.datetime.now().strftime('%H:%M:%S')
            
    except Exception, e:
        print e.message
       
def search_product_page_by_list(search_keywords, item_title, country_code, asin):
    
    for keywords in search_keywords:
#         print keywords
        print search_product_page(keywords, item_title, country_code, asin)
        time.sleep(10)
    
    
    
     



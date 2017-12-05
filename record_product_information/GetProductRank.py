# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-08-25 22:19:42
# @Last modified by:   LC
# @Last Modified time: 2016-09-02 22:09:13
# @Email: liangchaowu5@gmail.com

from selenium import webdriver
from bs4 import BeautifulSoup
import time



# PhantomJS 无法完全解释，某些项无法获取
#driver = webdriver.PhantomJS(executable_path = r'H:/PythonModule/phantomjs/phantomjs-2.1.1-windows/bin/phantomjs.exe')
#item_keywords = 'Bestfy(TM) 2Pack 10FT Nylon Braided Lightning Cable'

def get_product_page(search_keywords, item_keywords):
    """find the page of an item described by item_keywords when searching with search_keywords
    
    Args:
        search_keywords (str): keywords to search items, joined by '+'
        item_keywords (str): words to describe an item, part of title of the item
    
    Returns:
        
    """
#     driver = webdriver.Firefox()
    driver = webdriver.Chrome('/Users/spring8743/Documents/workspace/chromedriver')
    found = False
    page = -1
    try:
#         for i in xrange(1,21):
#             target_url = 'https://www.amazon.co.uk/s/ref=sr_pg_%s?page=%s&keywords=%s&ie=UTF8'%(i, i, search_keywords)
#             driver.get(target_url)
#             text = driver.page_source
#             soup = BeautifulSoup(text, 'lxml')
#             titles = soup.find_all('h2')
#             for title in titles:
#                 if item_keywords in title.get('data-attribute', ''):
#                     print 'Page %s: Found'%i
#                     found = True
#                     print title.get('data-attribute')
#                     print target_url
#                     break
#             if found:
#                 page = i
#                 break
#             print 'Page %s: Not Found'%i
#         return page
        target_url = 'https://www.amazon.co.uk/s/ref=sr_pg_%s?page=%s&keywords=%s&ie=UTF8'%(1, 1, search_keywords)
        driver.get(target_url)
        nextPage = '#pagnNextString'
        
#         time.sleep(20)
        
        for i in xrange(1, 10):
            text = driver.page_source
            soup = BeautifulSoup(text, 'lxml')
            titles = soup.find_all('h2')
            for title in titles:
                if item_keywords in title.get('data-attribute', ''):
                    print 'Page %s: Found'%i
                    found = True
                    print title.get('data-attribute')
                    print target_url
                    
                    driver.find_element_by_link_text(item_keywords).click()
                    time.sleep(10)
                    
                    cart = '#add-to-cart-button'
                    try:
                        driver.find_element_by_css_selector(cart).click()
                        print '================successfully add to cart==================='
                        time.sleep(5)
                    except Exception,e:
                            print 'Error while adding item to cart\n%s'%e.message
                            
                    
                    break
            if found:
                page = i
                break
            else:
                print 'Page %s: Not Found'%i
                driver.find_element_by_css_selector(nextPage).click()
                time.sleep(20)
                
            
        return page
            
    except Exception, e:
        print e.message
#     finally:
# #         driver.quit()
#         print 'quit'


def add_to_cart(self):
        """add item to cart"""
        cart = '#add-to-cart-button'
        try:
            self.driver.find_element_by_css_selector(cart).click()
            print '================successfully add to cart==================='
            time.sleep(5)
        except Exception,e:
            print 'Error while adding item to cart\n%s'%e.message
            self.exit_driver()
           
        
        
        
if __name__ == '__main__':

    search_keywords = 'digital+voice+recorder+8gb'
    item_keywords = 'Digital voice recorder, DREAMRY 8GB 1536Kbps USB Sound Audio Recorder Multifunctional Portable HD Recording Double Microphone Rechargeable Dictaphone/Noise Cancelling/Voice Activated/LCD Screen, Digital Audio MP3 Player for Recording Interviews, Meeting, Class, Lectures, Conferences and Conversation (Black)'
    
    get_product_page(search_keywords, item_keywords)



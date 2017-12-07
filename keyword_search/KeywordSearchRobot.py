# -*- coding: utf-8 -*-
'''
Created on 2017年12月2日

@author: spring8743
'''

from KeywordSearchSimulation import search_product_page_by_list
from keyword_rank.ListingTitle import voice_recorder_title
from keyword_rank.ListingTitle import country_code
from keyword_rank.ListingTitle import asin
from ProxyList import proxy_list



if __name__ == '__main__':
    
    for proxy in proxy_list:
        search_product_page_by_list([{'sightsky digital voice recorder':'long tail keyword'}], voice_recorder_title, country_code, asin, proxy)
    

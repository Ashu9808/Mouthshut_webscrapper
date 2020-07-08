#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:28:26 2020

@author: ashu
"""


import requests
from bs4 import BeautifulSoup
from nltk import word_tokenize
import numpy as np
from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import argparse


# for reading argument from the command line and converting into python objects
parser = argparse.ArgumentParser()
parser.add_argument('--out-dir',dest = 'output_dir_path',type = str, metavar = '<str>',required = True, help ='Path of the output file')
parser.add_argument('--url', dest = 'url', type = str, metavar = '<str>',required = True,help = 'website url from to be scrapped' )
parser.add_argument('--page',dest = 'no_pages',type = int, metavar = '<int>',required = True,help = 'Number of pages to be scraped')
args = parser.parse_args()




# chrome option for disabling notifications while scrapping
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 1 })

# chrome driver path 
driver = webdriver.Chrome(chrome_options=option,executable_path="/usr/lib/chromium-browser/chromedriver")

pages = np.arange(1,args.no_pages) #page_list


with open(args.output_dir_path,'w') as g:
    for page in pages:
        url = args.url+'-page-'+str(page)
        
    
        driver.get(url)
        
        try:
            for elem in driver.find_elements_by_link_text('Read More'): # for enabling mouse over actions (clicking read more button)
                elem.click()
                sleep(0.2) # enabling some lag for making lesser no. of Http request to the server
                
                
            with open('page_source.html', 'w') as f:
                f.write(driver.page_source)
                with open('page_source.html','r') as o:
                    html_soup = BeautifulSoup(o,'html.parser')
                    data_containers = html_soup.find_all('div',class_='row review-article')
                    
                    for container in data_containers:
                        d = container.find('div',class_='more reviewdata').text
                        g.write(d+'\n')
                        
        except:
            print('error')
    

    
    
    
    
    














    







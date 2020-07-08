# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:24:09 2020

@author: Edgar
"""

import urllib.request
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.options import Options

# opts = Options()

# opts.add_argument("user-agent='DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)'")

# driver = webdriver.Chrome(chrome_options=opts)

ua = UserAgent()

# url = 'https://www.lacentrale.fr/listing?makesModelsCommercialNames=FIAT%3A126'

# user_agent = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
# request = urllib.request.Request(url,headers={'User-Agent': user_agent})
# response = urllib.request.urlopen(request)
# html = response.read()
# Html_file= open("html_la_centrale.html","w")
# Html_file.write(str(html))
# Html_file.close()

def change_page(url,page):
    # print(page)
    driver.execute_script("javascript:ctrl.set_pageReload({})".format(page))
    # print("All pages downloaded")
    # driver.close()
def launch_request(url):
    driver = webdriver.Chrome()
    driver.get(url)
    
def get_html_download(url,page=1):
    # user_agent = 'DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)'
    # request = urllib.request.Request(url,headers={'User-Agent': user_agent})
    # response = urllib.request.urlopen(request)
    # html = response.read()
    
    html = driver.page_source
    # proper_html= html.encode('utf8')
    Html_file= open("html_le_parking_{}.html".format(page),"w")
    Html_file.write(str(html))
    
    change_page(url,page+1)
    # driver.execute_script("javascript:ctrl.set_pageReload({})".format(page+1))
    # get_html_download(driver.execute_script("javascript:ctrl.set_pageReload({})".format(page+1)),page)
    
def close_request():
    Html_file.close()

# url = 'https://www.otomoto.pl/osobowe/fiat/126/?search%5Bnew_used%5D=on'

# user_agent = 'DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)'
# request = urllib.request.Request(url,headers={'User-Agent': user_agent})
# response = urllib.request.urlopen(request)
# html = response.read()
# Html_file= open("html_otomoto.html","w")
# Html_file.write(str(html))
# Html_file.close()

# url = 'https://www.leboncoin.fr/recherche/?category=2&text=fiat%20126'

# user_agent = 'ia_archiver-web.archive.org '
# request = urllib.request.Request(url,headers={'User-Agent': user_agent})
# response = urllib.request.urlopen(request)
# html = response.read()
# Html_file= open("html_le_bon_coin.html","w")
# Html_file.write(str(html))
# Html_file.close()
    
url = 'https://www.leparking.fr/voiture-occasion/fiat-126.html'

launch_request(url)


get_html_download(url)

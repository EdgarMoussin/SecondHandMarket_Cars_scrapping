 # -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:45:51 2020

@author: Edgar
"""
import urllib.request
from fake_useragent import UserAgent
import scrapy
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class CarSpider(scrapy.Spider):
    name = 'cars'
    # start_urls = ['https://www.leparking.fr/voiture-occasion/fiat-126.html']
    # start_urls = ['https://www.leparking.fr/voiture-occasion/triumph-spitfire.html%3Fid_pays%3D18']
    # start_urls = ['https://www.leparking.fr/voiture-occasion/jaguar-type-E.html']
    start_urls = ['https://www.leparking.fr/voiture-occasion/mini-cooper-cabrio-france-essence.html']
    driv = webdriver.Chrome("C:/Users/alldocube/Desktop/Car_analysis_project/Algorithm/chromedriver.exe")
    
    def change_page(self,page,driver=driv):
        if page <= 40:
            driver.execute_script("javascript:ctrl.set_pageReload({})".format(page))
            self.get_html_download(page)
            return True
        else:
            print("All pages downloaded")
            return None

    def get_html_download(self,page=1,driver=driv):
        html = driver.page_source
        # proper_html= html.encode('utf8')
        # Html_file= open("html_le_parking_{}.html".format(page),"w")
        # Html_file.write(str(proper_html))
        # Html_file.close()
        return html
        
    
    def close_request(self,driver=driv):
        driver.close()
       
    def launch_request(self,url,driver=driv):
        # driver = webdriver.Chrome()
        driver.get(url)
              
    def parse(self, response,url=start_urls[0],driver=driv):
        # for car in response.xpath('//*[@class="market-price"]') :
        self.launch_request(url)
        condition = True
        page = 1
        dico = {}
        dico['Annee'] = []
        dico['Boite'] = ['-']
        dico['Pays'] = []
        dico['Code postal'] = []
        dico['Lien annonce'] = []
        dico['KM'] = []
        dico['Prix'] = []
        dico['Page'] = [page]
        while condition == True:
            List_prix = driver.find_elements_by_xpath('//*[@id="resultats"]/*[not(self::li[@class="premium-bloc li-result"])]//p[@class="prix"]')
            List_KM = driver.find_elements_by_xpath('//*[@id="resultats"]/*[not(self::li[@class="premium-bloc li-result"])]//li[2]/div[@class="upper"]')
            List_annee = driver.find_elements_by_xpath('//*[@id="resultats"]/*[not(self::li[@class="premium-bloc li-result"])]//li[3]/div[@class="upper"]')
            List_boite = driver.find_elements_by_xpath('//*[@id="resultats"]/*[not(self::li[@class="premium-bloc li-result"])]//li[4]/div[@class="upper"]')
            List_pays = driver.find_elements_by_xpath('//*[@id="resultats"]/*[not(self::li[@class="premium-bloc li-result"])]//div[@class="location"]/span[2]')
            List_code_postal = driver.find_elements_by_xpath('//*[@id="resultats"]/*[not(self::li[@class="premium-bloc li-result"])]//li[5]/div[@class="upper"]')
            List_lien_annonce = driver.find_elements_by_xpath('//*[@id="resultats"]/*[not(self::li[@class="premium-bloc li-result"])]//p[@class="link-mysite tag_f_list"]/a[1]')
            for i in range(len(List_prix)) :
                if List_prix[i].text != '' :
                    dico['Prix'].append(List_prix[i].text)
            for j in range(len(List_KM)) :
                dico['KM'].append(List_KM[j].text)
                dico['Annee'].append(List_annee[j].text)
                dico['Boite'].append(List_boite[j].text)
                dico['Pays'].append(List_pays[j].text)
                dico['Code postal'].append(List_code_postal[j].text)
                dico['Lien annonce'].append(List_lien_annonce[j].get_attribute("href"))
            dico['Page'][0]=page
            print(dico)
            # driver.implicitly_wait(2)
            condition = self.change_page(page+1)
            page +=1
        self.close_request()
        yield dico
        # yield {response.xpath('//*[@id="resultats"]/script[23]/text()').getall()}  obtaining dictionnary of the whole annouce (NOT WORKING)
       
        
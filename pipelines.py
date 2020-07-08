# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import xlwt

class AlgorithmPipeline(object):
    def process_item(self, item, spider):
        # path = "C:/Users/alldocube/Desktop/Car_analysis_project/Algorithm/resultats_le_parking_Fiat_126_monde.xls"
        # path = "C:/Users/alldocube/Desktop/Car_analysis_project/Algorithm/resultats_le_parking_spitfire_france.xls"
        # path = "C:/Users/alldocube/Desktop/Car_analysis_project/Algorithm/resultats_le_parking_jaguar_type_E_france.xls"
        path = "C:/Users/alldocube/Desktop/Car_analysis_project/Algorithm/resultats_le_parking_mini_cooper_cabrio_france.xls"
        classeur = xlwt.Workbook()
        feuille1 = classeur.add_sheet("resultats")
        
        i = 0
        for key, value in item.items():
            feuille1.write(0,i,label=key)
            j = 0
            for j in range(len(value)):
                # if value[j].endswith('KM'):
                #     value[j]=value[j].replace("KM","")
                # if value[j].endswith('€'):
                #     value[j]=value[j].replace("€","")
                feuille1.write(j+1,i,label=value[j])
            i+=1
        classeur.save(path)
        return item

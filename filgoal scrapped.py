# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 16:39:17 2023

@author: zeyad
"""

from bs4 import BeautifulSoup
import csv
import requests

date=input('please enter the following date YYYY-MMMM-DDDD ')
url=f'https://www.filgoal.com/matches/?date={date}'
page=requests.get(url)


def main(page):
    
    src=page.content
    soup=BeautifulSoup(src,'lxml')
    championships=soup.find_all('div',{'class':"mc-block"})
    matches_details=[]
    def match_info(championships):
        
        champion_title=championships.find('h6').text.strip()
        all_matches=championships.find_all('div',{'class':"cin_cntnr"})
        num_matches=len(all_matches)
        for i in range(num_matches):
            teamA= all_matches[i].find('div',{'class':"f"}).text.strip()
            teamb= all_matches[i].find('div',{'class':"s"}).text.strip()
            match_time=all_matches[i].find('div',{'class':'m'}).find('span',{'class':'status'}).text
            match_result=all_matches[i].find('div',{'class':'match-aux'}).text
            matches_details.append({'first team':teamA,'second team':teamb,'time':match_time,'result':match_result})
            
    for champion in range( len(championships)) :  
        match_info(championships[champion])
    
    keys=matches_details[0].keys()
    with open(r'C:\Users\zeyad\OneDrive\Desktop\filgoalgames.csv','w',encoding='utf-8-sig',newline='')as filgoal:
       
        dictwriter=csv.DictWriter(filgoal,keys) 
        dictwriter.writeheader()
        dictwriter.writerows(matches_details)
    
main(page)





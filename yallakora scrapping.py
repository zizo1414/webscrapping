# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:34:12 2023

@author: zeyad
"""

import requests
import csv
from bs4 import BeautifulSoup

date = input('Please enter the date following MM/DD/YYYY: ')
url = f'https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}'
page = requests.get(url)


def main(page):
    src = page.content
    soup = BeautifulSoup(src, 'lxml')
    match_details = []
    championships = soup.find_all('div', {'class': 'matchCard'})

    def match_info(championship):
        championship_title = championship.contents[1].find('h2').text.strip()
        all_matches = championship.contents[3].find_all('li')
        num_matches = len(all_matches)
        for i in range(num_matches):
            teamA = all_matches[i].find('div', {'class': 'teams teamA'}).text.strip()
            teamB = all_matches[i].find('div', {'class': 'teams teamB'}).text.strip()
            match_result = all_matches[i].find('div', {'class': 'MResult'}).find_all('span', {'class': 'score'})
            score = f"{match_result[0].text.strip()} ------ {match_result[1].text.strip()}"
            match_time = all_matches[i].find('div', {'class': 'MResult'}).find('span', {'class': 'time'}).text.strip()
            match_details.append({'Championship': championship_title, 'Team A': teamA, 'Team B': teamB, 'Match Time': match_time, 'Score': score})
    
    for championship in championships:
        match_info(championship)
    
    keys = match_details[0].keys() 
    with open(r'C:\Users\zeyad\OneDrive\Desktop\games.csv', 'w', encoding='utf-8-sig', newline='') as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(match_details)


# Assuming you already have the 'page' variable defined
main(page)

date=input("please enter the following date in this format MM-DDDD-YYYY")
# url =requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}")

# def main (url):
    
# this another similiar script but with some differences as i tried  to run the script but i found some  type error  actually 
#     src=url.content
#     soup=BeautifulSoup(src,'lxml')
    
#     championships=soup.find_all('div',{'class':'matchCard'})
#     def champion(championships):
#         champion_title=championships[1].find('h2').text
#         matches_details=championships[3].find_all('div')
#         numberof_matches= len(matches_details)
         
#         for i in range(numberof_matches) :
            
#             first_team=matches_details[i].find('div',{'class':'teams teamA'}).text.strip() if matches_details[i].find('div',{'class':'teamsData'}) else "^^^^^^"
    
#             second_team=matches_details[i].find('div',{'class':'teams teamB'}).text.strip() if matches_details[i].find('div',{'class':'teams teamB'})else "^^^^^^^"
#             match_result=matches_details[i].find('div',{'class':'MResult'})
#             # Check if match_result is not None
#             if match_result is not None:
#                 score=match_result.find_all('span',{'class':'score'})
#                 score=f"{score[0].text}  ________  {score[1].text}"
#                 match_time=match_result.find('span',{'class':'time'}).text if match_result.find('span',{'class':'time'}) else "^^^^^^^^^^"
#                 matches.append({'firsteam':first_team,'second_time':second_team,
#                                 'result':score,'time':match_time})
        
            
#     champion(championships)
#     keys=matches[0].keys()
#     with open(r'C:\Users\zeyad\OneDrive\Desktop\games.csv','w'  ,newline='', encoding='utf-8-sig')as game :
#         all_games=csv.DictWriter(game,keys)
#         all_games.writerows(matches)
        
# main(url)











 



































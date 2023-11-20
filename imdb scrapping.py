# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 11:53:37 2023

@author: zeyad
"""
import numpy as np
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
movies=[]
year=[]
time=[]
rating=[]
metascore=[]
votes=[]
gross=[]


page=requests.get(r'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating')
src=page.content
soup=BeautifulSoup(src,'lxml')
print(soup)


movie_df=soup.find_all('div',{'class':'lister-item mode-advanced'})



for movie in movie_df :
    
    movie_name=movie.find('h3').find('a').text
    movies.append(movie_name)
    
    movie_years= movie.find('h3').find('span',{'class':'lister-item-year text-muted unbold'}).text.replace('(','').replace(')','')
    year.append(movie_years)

    movie_time=movie.find('p').find('span',{'class':'runtime'}).text.replace('min','MINUTES')
    time.append(movie_time)
    
    movie_ratings=movie.find('div',{'class':'ratings-bar'}).find('div',{'class':'inline-block ratings-imdb-rating'}).text.replace('\n','')
    
    rating.append(movie_ratings)

    movie_meta=movie.find('span',{'class':'metascore'}).text.strip() if movie.find('span',{'class':'metascore'})  else '****'
    
    
    metascore.append(movie_meta)

    movie_value= movie.find_all('span',attrs={'name':'nv'})
   
   
    values=   movie_value[0].text
    votes.append(values)
    grosss=    movie_value[1].text if len(movie_value)>1 else '^^^^'
    gross.append(grosss)
    
   
 
df=pd.DataFrame({'name-of-the-movie':movies,'production year':year,'duration':time,'rating':rating,'score':metascore,'value':'votes','total gross':gross})
    



print(df)
df.columns

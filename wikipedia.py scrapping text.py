# -*- coding: utf-8 -*-
"""
#scrapping data from hand scrapper wikepedia 

import numpy as np
import pandas as pd
import requests 
import csv
import requests
from bs4 import BeautifulSoup


url=requests.get('https://en.wikipedia.org/wiki/Hand_scraper')

src=url.content
soup=BeautifulSoup(url.text,'html.parser')

for paragraph in soup.select('p') :
    
    print(paragraph)
    

with open(r"C:\Users\zeyad\OneDrive\Desktop\scraped_text.txt", "w", newline="") as f:
  writer = csv.writer(f)
  for paragraph in soup.select('p'):
    writer.writerow([paragraph])
"""
    


#scrapping data from egypt wikepdia 


import numpy as np
import pandas as pd
import requests 
import csv
import requests
from bs4 import BeautifulSoup



page=requests.get('https://en.wikipedia.org/wiki/Egypt')

soup=BeautifulSoup(page.text,'html.parser')



 
    
with open(r'C:\Users\zeyad\OneDrive\Desktop\egypt_text.txt','w',newline='',encoding='utf-8')as file :
    
    
    writer=csv.writer(file)
    
    for paragraph in soup.select('p'):

       writer.writerow([paragraph])


    
    

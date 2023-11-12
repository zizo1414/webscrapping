# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:15:11 2023

@author: zeyad
"""


    
    
    
    
    
    
    
import csv
import requests
from bs4 import BeautifulSoup

jobtitle = []
joblocation = []
companyname = []
skills = []
links = []
salaries = []
requirements = []
responsibilities = []
date = []

url = 'https://wuzzuf.net/search/jobs/?q=python+developer&a=navbl'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

job_title = soup.find_all('h2', {'class': 'css-m604qf'})
company_name = soup.find_all('a', {'class': 'css-17s97q8'})
company_location = soup.find_all('span', {'class': 'css-5wys0k'})
job_skills = soup.find_all('div', {'class': 'css-y4udm8'})
new_date = soup.find_all('div', {'class': 'css-4c4ojb'})
old_date = soup.find_all('div', {'class': 'css-do6t5g'})
all_dates = [*new_date, *old_date]

for i in range(len(job_title)):
    jobtitle.append(job_title[i].text.strip())
    companyname.append(company_name[i].text.strip())
    joblocation.append(company_location[i].text.strip())
    skills.append(job_skills[i].text.strip())
    links.append(job_title[i].find('a').attrs['href'])
    date.append(all_dates[i].text.strip())

for link in links:
    url = requests.get(link)
    src = url.content
    soup = BeautifulSoup(src, 'lxml')
    salary = soup.find_all('span', {'class': 'css-47jx3m'})
    salaries.append(salary)
    
    requirements_elem = soup.find('div', {'class': 'css-1t5f0fr'})
    if requirements_elem:
        requirements_list = requirements_elem.find_all('li')
        requirements_text = ', '.join([li.text.strip() for li in requirements_list])
        requirements.append(requirements_text)
    else:
        requirements.append('N/A')
    
    responsibilities_elem = soup.find('div', {'class': 'css-1uobp1k'}).find_all('li') if soup.find('div', {'class': 'css-1uobp1k'}) else []
    if responsibilities_elem:
        responsibilities_text = ', '.join([li.text.strip() for li in responsibilities_elem])
        responsibilities.append(responsibilities_text)
    else:
        responsibilities.append('N/A')

# Export data to a CSV file
data = zip(jobtitle, joblocation, companyname, skills, links, salaries, requirements, responsibilities, date)
with open(r'C:\Users\zeyad\OneDrive\Desktop\example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Job Title', 'Location', 'Company Name', 'Skills', 'Links', 'Salary', 'Requirements', 'Tasks', 'Date'])
    writer.writerows(data)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
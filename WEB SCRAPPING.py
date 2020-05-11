#!/usr/bin/env python
# coding: utf-8

# # EXTRACTING INFORMATION REGARDING SOME OF THE MOVIES FROM THE SITE OF IMDB USING WEB SCRAPPING

# In[1]:


# import all required library
import random
import urllib.request
from urllib import request


# In[2]:


# web scraping 
from bs4 import BeautifulSoup


# In[3]:


import urllib.request as urllib2
from urllib.request import urlopen


# # Movie title and some detial from IMDB

# In[7]:


imdb = "https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=8a7876cd-2844-4017-846a-2c0876945b7b&pf_rd_r=J22VX3EAQ895AXN10EBY&pf_rd_s=right-5&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_india_tr_rhs_1"


# In[8]:


web = urlopen(imdb)


# In[9]:


web = BeautifulSoup(web, "lxml")


# In[10]:


movie_name = []
movie_site = []
release_year = []
imdb_rating = []
for table in web.findAll('table', class_ = 'chart full-width'):
    for body in table.findAll('tbody', class_ = "lister-list"):
        for row in body.findAll('tr'):
            for column in row.findAll('td', class_ = "titleColumn"):
                for link in column.findAll('a'):
                    movie_name.append(link.text)
                    b = "https://www.imdb.com"+link.get('href')
                    movie_site.append(b)
                for year in column.findAll('span', class_ = 'secondaryInfo'):
                    release_year.append(year.text)
            for imdB in row.findAll('td', class_ = "ratingColumn imdbRating"):
                imdb_rating.append(imdB.text)


# # Total_number of movies list

# In[11]:


len(movie_name)


# In[12]:


movie_name


# In[13]:


for i in movie_site:
    print(i)


# In[ ]:


movie_time = []
release_date = []
for i in movie_site:
    sourcecode = urlopen(i)
    soup = BeautifulSoup(sourcecode, "lxml")
    for div in soup.findAll('div', class_ = "subtext"):
        for time in div.findAll('time'):
            movie_time.append(time.text)
        for date in div.findAll('a', {'title' : 'See more release dates'}):
            release_date.append(date.text)


# In[ ]:


movie_genre


# In[ ]:


rating_count = []
for i in movie_site:
    sourcecode = urlopen(i)
    soup = BeautifulSoup(sourcecode, "lxml")
    for div1 in soup.findAll('div', class_ = "imdbRating"):
        for lin in div1.findAll('span', class_ = "small"):
            rating_count.append(lin.text)


# In[ ]:


movie_genre = []
for i in movie_site:
    sourcecode = urlopen(i)
    soup = BeautifulSoup(sourcecode, "lxml")
    for div in soup.findAll('div', class_ = "subtext"): 
        for genr in div.findAll('a'):
            movie_genre.append(genr.text)


# In[23]:


director_name = []
for i in movie_site:
    sourcecode = urlopen(i)
    soup = BeautifulSoup(sourcecode, "lxml")   
    for div2 in soup.findAll('div', class_ = "credit_summary_item"):
        for dirc in div2.findAll('span', {'itemprop' : 'director'}):
            director_name.append(dirc.text)


# In[ ]:


director_name


# In[ ]:


# Convert into CSV
import pandas as pd


# In[ ]:


movies_csv = pd.DataFrame(movie_name, columns = ['Movies_title'])
movies_csv['Release Date'] = release_date
movies_csv['Release Year'] = release_year
movies_csv['IMDB Rating'] = imdb_rating
movies_csv['Time Length'] = movie_time
movies_csv['Rating Count'] = rating_count
movies_csv['Site'] = movie_site


# In[28]:


writer = pd.ExcelWriter('movies.xlsx')
movies_csv.to_excel(writer,'Sheet1')
writer.save()


# In[29]:


movies_csv


# In[ ]:





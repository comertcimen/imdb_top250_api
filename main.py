import requests
from bs4 import BeautifulSoup
import re
from typing import Optional
from fastapi import FastAPI


#Scraper


res = requests.get("https://www.imdb.com/chart/top/")
src = res.content
soup = BeautifulSoup(src, 'lxml')
data = soup.find('tbody', {'class': 'lister-list'})
trs = data.findAll('tr')

api = []



for tr in trs:
    movie_title = tr.find('img').attrs["alt"]
    movie_poster = tr.find('img').attrs["src"]
    movie_rank = tr.find('span', {'name': 'rk'}).attrs["data-value"]
    release_year = re.sub('\D', '', (tr.find('span', {'class': 'secondaryInfo'}).text))
    rating = tr.find('strong').text
    imdb_id = re.search('tt.\d{6}', tr.find('a').attrs["href"]).group()
    api.append({
    	'imdb_rank': movie_rank,
    	'title': movie_title,
    	'poster': movie_poster,
    	'release_year': release_year,
    	'rating': rating,
    	'imdb_id': imdb_id
    	})


#FastAPI

app = FastAPI()

@app.get("/")
def read_root():
	return(api)

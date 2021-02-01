# web scrapping table data from: https://keithgalli.github.io/web-scraping/webpage.html

# load packages we will use
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# url = 'https://keithgalli.github.io/web-scraping/webpage.html'

def get_webpage(url):
# make the request
    r=requests.get(url)
# create a beautiful soup object named 'webpage' with using bs() on 'r'.
    webpage=bs(r.content, features='lxml')
    return(webpage)

# test
# get_webpage(url)




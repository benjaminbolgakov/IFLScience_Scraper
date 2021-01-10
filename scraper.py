#!/usr/bin/env/ python3
import requests
from bs4 import BeautifulSoup
url = "https://www.iflscience.com/"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')

article_list = soup.find_all("h3", "title")

title_raw = []
link_list = []
articles = {}

#Function returning a formated url from the raw string data
##Defines a scope between the two first occuring " characters
###and returns the data within as the formatted_url
def url_formatted(url_raw):
        link_index_start = url_raw.find('"')+1
        link_index_end = url_raw.find('"', link_index_start)
        formatted_url = url_raw[link_index_start:link_index_end]
        return formatted_url

#Insert article data into dict for future use
dict_index = 0;
for items in article_list:
        title_string = str(items.text)
        link_string = str(items.find_all("a"))
        dict_index = article_list.index(items)
        articles[dict_index] = {
                "title": title_string,
                "url": url_formatted(link_string)}
        print(articles[dict_index]["title"])

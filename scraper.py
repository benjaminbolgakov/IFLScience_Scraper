#!/usr/bin/env/ python3
import requests
import formatter
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


for article_items in article_list:
	title_string = str(article_items.text)
	link_string = str(article_items.find_all("a"))
	articles[article_list.index(article_items)] = {
		"title": title_string,
		"url": url_formatted(link_string)
	}

print(articles)


##Testing <------------------------------------------------------------->
"""
for article_items in article_list:
	link_list.append(article_items.find_all("a"))
	title_raw.append(article_items.text)


#Title-text from articles
title_string = str(title_raw[0])
print(title_string + "\n")

#URL's from articles
link_string = str(link_list[0])
print(link_string + "\n")

#Find index where url starts
link_index_start = link_string.find('"')+1
print("index start:  ", link_string.find('"')+1)

#Find index where url ends
link_index_end = link_string.find('"', link_index_start)
print("index end:    ", link_string.find('"', link_index_start))

#Cut out url
link_formatted = link_string[link_index_start:link_index_end]
print(link_formatted)


##Datastructure

articles = {
	"article" : {
		"title": title_string,
		"link": link_formatted
	}
}

for article_title, article_link in articles.items():
	print(article_title)
	print(article_link)
"""
##Testing <------------------------------------------------------------->
import json
import requests
import sys

def newsAPI(keyword: str):

	url = ('http://newsapi.org/v2/everything?'
	       f'q={keyword}&'
	       'from=2020-06-18&'
	       'sortBy=relevancy&'
	       'apiKey={apiKey}')

	response = requests.get(url)

	return response.json()

def parseJSON(json: object):
	# print(json['articles'][1])
	articles = json['articles']
	stats = []
	for article in articles:
		artObj = {article['source']['name'] : article['title'], "contents" : article['description']}
		stats.append(artObj)	
	return artObj

def main():
	keyword = sys.argv[1]
	json = newsAPI(keyword)
	print(parseJSON(json))

main()

import json
import os

from newsapi import NewsApiClient

apiKey = "10adc7bd681d42eda0796b7c0424dcd3"

def getNews(keyword):
    if os.path.exists(keyword+"json"):
        return
    newsapi = NewsApiClient(api_key=apiKey)

    all_articles = newsapi.get_everything(q=keyword, language='en', sort_by='relevancy')

    with open(keyword+".json", "w") as f:
        f.write(json.dumps(all_articles))
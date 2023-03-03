from newsapi import NewsApiClient
import json

apiKey = "10adc7bd681d42eda0796b7c0424dcd3"

newsapi = NewsApiClient(api_key=apiKey)

all_articles = newsapi.get_everything(q='adani enterprise', language='en', sort_by='relevancy')

print(all_articles)
with open("test.json", "w") as f:
    f.write(json.dumps(all_articles))
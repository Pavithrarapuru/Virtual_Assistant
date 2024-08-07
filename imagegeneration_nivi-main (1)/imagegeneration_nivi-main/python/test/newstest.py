import json
import requests



def news():
    url='https://newsapi.org/v2/top-headlines?country=us&apiKey=54185350d5d74c809213488b6ce4fefc'
    req=requests.get(url)
    news=json.loads(req.text)
    formatted_news=[]
    for i,article in enumerate(news["articles"][:10],start=1):
        formatted_article=f"{i}.{article['title']}\n{article['description']}"
        formatted_news.append(formatted_article)
    print(formatted_news)
news()
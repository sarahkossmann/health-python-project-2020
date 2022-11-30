import requests
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health.settings')
django.setup()
import pprint
from news.models import News







url = ('http://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=957f7b195f254df898fe7542018a8a51')
response = requests.get(url)
info = response.json()

# title = info.get('article').get('title')

for i in info['articles']:
    title = i['title']
    author = i['author']
    description = i['description']
    url = i['url']
    image_url = i['urlToImage']
    published_date = i['publishedAt']
    content = i['content']

    # print(author)
    n = News(title=title, author=author, description=description, url=url, image_url=image_url, published_date=published_date, content=content)
    # n.save()




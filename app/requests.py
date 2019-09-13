# from app import app
import urllib.request,json
from .models import News,Articles


# News = news.News
# Getting api key
# api_key = app.config['NEWS_API_KEY']
api_key = None
# Getting the movie base url
base_url = None
# base_url = app.config["NEWS_API_BASE_URL"]
articles_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    # print(api_key)
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_sources = None

        if get_news_response['sources']:
            news_sources_list = get_news_response['sources']
            news_sources = process_results(news_sources_list)

    return news_sources

def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    '''

    news_sources = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        language = news_item.get('language')
        country = news_item.get('country')
        category = news_item.get('category')

        if name:
            news_object = News(id,name,description,url,category,country,language)
            news_sources.append(news_object)

    return news_sources

def get_articles(id):
 '''
 Function that processes the articles and returns a list of articles objects
 '''
 get_articles_url = articles_url.format(id,api_key)
 
 print(api_key)
 print(articles_url)
 with urllib.request.urlopen(get_articles_url) as url:
   articles_results = json.loads(url.read())
   articles_object = None
   if articles_results['articles']:
     articles_object = process_articles(articles_results['articles'])
 return articles_object
def process_articles(articles_list):
 '''
 '''
 articles_object = []
 for article_item in articles_list:
   id = article_item.get('id')
   author = article_item.get('author')
   title = article_item.get('title')
   description = article_item.get('description')
   url = article_item.get('url')
   image = article_item.get('urlToImage')
   date = article_item.get('publishedAt')
   if image:
     articles_result = Articles(id,author,title,description,url,image,date)
     articles_object.append(articles_result)
 return articles_object



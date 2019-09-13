# from app import app
import urllib.request,json
from .models import News

# News = news.News
# Getting api key
# api_key = app.config['NEWS_API_KEY']
api_key = None
# Getting the movie base url
base_url = None
# base_url = app.config["NEWS_API_BASE_URL"]


def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


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


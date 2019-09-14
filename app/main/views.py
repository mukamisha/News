from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_articles
# from .forms import ReviewForm
from ..models import News    

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting type of news i want
    general_news = get_news('entertainment')
    print(general_news)
    title = 'Home - Welcome to The best News Website Online'
    return render_template('index.html', title = title,general_news = general_news)

@main.route('/news/<id>')
def articles(id):
   '''
   view articles page
   '''
   print('test')
   print(id)
   articles = get_articles(id)
   
   title = f'MK | {id}'
   return render_template('articles.html',title= title,articles = articles)
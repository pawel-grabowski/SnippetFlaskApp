from app import app
from flask import render_template


@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Miguel'}
    list = ['aaa','bbb','ccc']
    return render_template('index.html', title='Home', user=user, list=list)
    
    
# @app.route('/show_snippet')
# def show_snippet():
#     #gist=
#     return
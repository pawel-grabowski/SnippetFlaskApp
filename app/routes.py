from app import app
from flask import render_template
from app import custom_func as cf

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Pawel'}
    file_path = "C:/Users/Paweł/Documents/Projekty/SnippetFlaskApp/snippets/"
    snippets_dict = cf.get_inner_dict(cf.load_all_files(file_path))
    
    list = cf.get_keys(snippets_dict) #['aaa','bbb','ccc']
    
    
    return render_template('index.html',
                           title='Simple SQL snippet manager',
                           user=user,
                           list=list,
                           content=snippets_dict)

# @app.route('/show_snippet')
# def show_snippet():
#     #gist=
#     return
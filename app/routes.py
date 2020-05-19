from app import app
from flask import render_template
from app import custom_func as cf

@app.route('/')
@app.route('/index') 

def index():
    user = {'username': 'Pawel'}
    snippets_dict={}
    
    with open('./config.txt', 'r', encoding='utf-8-sig') as f:
        lines=f.readlines()
        
    for line in lines:
        line = line.strip('\n')
        file_path=line.split('|')[0]

        if len(line.split('|'))>1:
            kodek=line.split('|')[1]
        else: kodek='utf-8'

        temp_dict = cf.get_inner_dict(cf.load_all_files(file_path,kodek))
        snippets_dict.update(temp_dict)
     
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
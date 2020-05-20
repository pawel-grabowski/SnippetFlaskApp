import re
import os

def read_files(file_path, kodek):
    
    try:
        with open(file_path, 'r', encoding=kodek) as f:
            content=f.read()
    except:
        print('Error while reading: ' + file_path + 'encoding: ' + kodek)
        
    return content
    
    
def split_files(content):
    # podzial na fragment wg z znacznika
    content = content.replace("\n/*",";\n<%stop%>/*") # SQL-JS
    content = content.replace("\n##",";\n<%stop%>##") # R
    content = content.replace("\n#%%",";\n<%stop%>#%%") # Py
    content = content.replace("\n#\s%%",";\n<%stop%>#\s%%") # Py
    content = content.replace("\n\'#",";\n<%stop%>\'#") # VBA
    
    splitted = content.split("<%stop%>")
    snippets = []
    
    for sn in splitted:
        
        header = re.search('\/\*(.+?)\*\/', sn) # SQL-JS
        if not header:
            header = re.search('#(.+?)----', sn) # R
        if not header:
            header = re.search('#%%(.+?)\n', sn) # Py
        if not header:
            header = re.search('# %%(.+?)\n', sn) # Py
        if not header:
            header = re.search('\'#(.+?)\n', sn) # VBA
        
        if header:
            header = header.group(1)
            
            snippet = {"title": header, "code": sn}
            snippets.append(snippet)
    
    return snippets
    

def get_titles_list(data):
    titles_list=[]
    for record in data:
        titles_list.append(record["title"])
        
    return titles_list

def get_snippet_dict(data):
    snippets={}
    for record in data:
        snippets.update({record["title"] : record["code"]})
        
    return snippets


def load_all_files(folder_path, kodek):
    files=os.listdir(folder_path)
    snippets_by_file = {}
    
    for file in files:
        file_path=os.path.join(folder_path,file)
        
        # przejście do kolejnej iteracji jeśli *file* jest folderem
        if os.path.isdir(file_path):
            continue
        
        
        temp = read_files(file_path, kodek)
        temp = split_files(temp)
        snippet_dict = get_snippet_dict(temp)
        snippets_by_file.update({file:snippet_dict}) # dictionary of dictionaries
    
    return snippets_by_file

def get_keys(dict): 
    return dict.keys() 


def get_inner_dict(dict):
    snippets_by_title={}
    
    for k in dict.keys():
        snippets_by_title.update(dict[k])
        
    return  snippets_by_title


if __name__ == "__main__":
    # a = read_files("C:/Users/Paweł/Documents/Projekty/SnippetFlaskApp/snippets/test.sql")
    # b = split_files(a)
    # c = get_titles_list(b)
    # d = get_snippet_dict(b)

    x = load_all_files("C:/Users/Paweł/Documents/Projekty/SnippetFlaskApp/snippets/", kodek='utf-8')
    print(get_keys(x))
    y = get_inner_dict(x)
   




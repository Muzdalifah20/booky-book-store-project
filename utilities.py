import json

def get_html(html_page):
    html_file = open("templates/"+html_page + ".html")
    content = html_file.read()
    html_file.close()
    return content

def usersdb():
    #  case the file is empty
    try:
          with open("usersdb.json","r") as file:
               users = json.load(file)
    except(FileNotFoundError):
          users = []
    return users
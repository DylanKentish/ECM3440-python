# bottle_httpd_demo.py
from bottle import route, run

@route('/')
def home():
    return '<h1>Homepage</h1>'

@route('/hello/<name>')
def hello(name):
    return f'<b>Hello {name}</b>!'

run(host='localhost', port=8080)

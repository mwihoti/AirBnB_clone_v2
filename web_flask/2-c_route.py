#!/usr/bin/python3
"""script that starts Flask"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Defines Hello function"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Defines hbnb function"""
    return 'HBNB'

@app.route('/c/<text>')
def c_text(text):
    """defines text function for url parameter"""
    return 'C {} '.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(debug=True)

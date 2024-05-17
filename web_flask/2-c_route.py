#!/usr/bin/python3
"""script that starts Flask"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def text():
    return 'C'

if __name__ == '__main__':
    app.run(debug=True)

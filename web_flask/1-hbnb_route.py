#!/usr/bin/python3
"""script that starts Flask"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """hello function"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """HBNB function"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(debug=True)

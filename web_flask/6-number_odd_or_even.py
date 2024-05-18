#!/usr/bin/python3
"""script that starts Flask"""
from flask import Flask, render_template


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
    """defines c_text function for url parameter"""
    return 'C {} '.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def py_text(text):
    """defines py_text function for url parameter"""

    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def n_num(n):
    """Define n_num function"""
    return '{} is a number'.format(n)


@app.route('/number_template/<n>')
def template(n):
    """Define template function  Prints n if its an integer"""
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<n>')
def num_Check(n):
    """Defines num_Checkfunction Checks if n is odd number or even"""
    if n % 2 == 0:
        num_is = "even"
    else:
        num_is = 'odd'
    return render_template('6-number_odd_or_even.html', num=n, num_is = num_is)

if __name__ == '__main__':
    app.run(debug=True)

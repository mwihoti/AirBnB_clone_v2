#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_storage(exception=None):
    """removes the current SQLAlchemy Session
    """
    if storage is not None:
        storage.close()


@app.route('/cities_by_states')
def cities_list(n=None):
    """displays a HTML page: inside the tag BODY"""
    # check 8-cities.py and html for another way to do this
    states = storage.all(State).values()
    sorted_state = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_state)


if __name__ == '__main__':
    app.run(debug=True)

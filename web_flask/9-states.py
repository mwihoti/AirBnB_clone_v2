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


@app.route('/states')
def states():
    """Display a HTML page with the list of all states"""
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states_sorted)


@app.route('/states/<id>')
def state_cities(id):
    """Display a HTML page with the state and its cities if found,
    otherwise 'Not found'"""
    state = storage.all(State).get('State.' + id)
    if state:
        cities = list(state.cities)
        cities.sort(key=lambda city: city.name)
        return render_template('9-state.html', state=state, cities=cities)
    else:
        return render_template('9-not_found.html')


if __name__ == '__main__':
    app.run(debug=True)

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


@app.route('/states_list')
def states_list():
    """display a HTML page: (inside the tag BODY"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(debug=True)

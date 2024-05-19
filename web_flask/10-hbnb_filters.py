#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_storage(exception=None):
    """removes the current SQLAlchemy Session
    """
    if storage is not None:
        storage.close()

@app.route('/hbnb_filters')
def hbnb_filters(id=None):
    """displays a HTML page: inside the tag BODY"""
    states = storage.all(State).values()
    sorted_state = sorted(states, key=lambda state: state.name)
    amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(amenities, key=lambda Amenity: Amenity.name)
    return render_template('10-hbnb_filters.html',
                           states=sorted_state, amenities=sorted_amenities)


if __name__ == '__main__':
    app.run(debug=True)

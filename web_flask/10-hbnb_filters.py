#!/usr/bin/python3
"""script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def index():
    """Filters"""
    states = storage.all(State).values()
    amenitys = storage.all(Amenity).values()
    return render_template('6-index.html', states=states, amenitys=amenitys)


@app.teardown_appcontext
def teardown(self):
    """Close session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""
starts with flask
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """return a message"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hi_HBNB():
    """Display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def redirect_parameter(text):
    """Accept parameter"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False, defaults={'text': "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Python is cool"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n: int):
    """Return number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Handling templates"""
    context = {'n': n}
    return render_template('5-number.html', **context)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_template2(n):
    """Handling templates"""
    context = {'n': n}
    return render_template('6-number_odd_or_even.html', **context)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

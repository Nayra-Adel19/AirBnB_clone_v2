#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ starts a Flask web application """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ starts a Flask web application """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ starts a Flask web application """
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """ starts a Flask web application """
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    """ starts a Flask web application """
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ starts a Flask web application """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ starts a Flask web application """
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == '__main__':
    """ starts a Flask web application """
    app.run(host='0.0.0.0', port=5000)

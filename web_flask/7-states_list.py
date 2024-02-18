#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ starts a Flask web application """
    sortedlist = sorted(storage.all(
        State).values(), key=lambda x: x.name)
    return render_template("7-states_list.html", sorted_states_list=sortedlist)


@app.teardown_appcontext
def terminate(exc):
    """ starts a Flask web application """
    storage.close()


if __name__ == '__main__':
    """ starts a Flask web application """
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, url_for
from operations import *

app = Flask(__name__)


@app.route('/add')
def add():
    return f"{int(request.args['a']) + int(request.args['b'])}"


@app.route('/subtract')
def subtract():
    return f"{int(request.args['a']) - int(request.args['b'])}"


@app.route('/multiply')
def multiply():
    return f"{int(request.args['a']) * int(request.args['b'])}"

@app.route('/divide')
def divide():
    return f"{int(request.args['a']) / int(request.args['b'])}"



app.run(debug=True)

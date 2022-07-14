from flask import Flask
import flask
from markupsafe import escape, Markup

app = Flask(__name__)


@app.route('/<name>')
def hello(name):
    print(name)
    return f"Hello, {escape(name)}!"
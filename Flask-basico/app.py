from flask import Flask
import flask
from markupsafe import escape, Markup

app = Flask(__name__)


@app.route('/<name>')
def hello(name):
    print(name)
    return f"Hello, {escape(name)}!"

# Tipos de convertidores 
    """
        string
        int
        float
        path
        uuid
    """
    
 
#Reglas de variables   
@app.route('/user/<username>')
def username(username):
    ...
    
@app.route('/post/<int:post_id>')
def post(post_id):
    ...
    
@app.route('/path/<path:subpath>')
def method_name(subpath):
    ...

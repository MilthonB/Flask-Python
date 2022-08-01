from urllib import response
from flask import Flask, render_template, request, Response, Request
import flask
from flask import url_for
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
    
# Regla de dos diagonales o una 
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


# Creacion de endpoint y sus elementos
@app.route('/')
def index():
    # Mensajes a nivele consola 
    app.logger.debug(f"Path del endpoint: {request.path}")
    app.logger.debug(f"Mensaje a nivel de Debug {request.path}")
    app.logger.info("Mensaje a nivel de Debug")
    app.logger.warn("Mensaje a nivel de Debug")
    app.logger.error("Mensaje a nivel de Debug")
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user1/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    
@app.route('/saludard')
def saludar():
    return 'Hola, estoy saludando'

@app.route('/saludar/<nombre>')
def saludar_nombre(nombre):
    return f'Hola, estoy saludand, soy: {nombre}'


# Todos los return deben de ser strings
@app.route('/multi/<int:numero>')
def multiplica(numero):
    return f'{2*numero}'

@app.route('/edad/<int:edad>')
def mostar_edad(edad):
    return f'La edad es de {edad}'




@app.route('/render')
def render():
    return render_template('index.html')
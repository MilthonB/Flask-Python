from crypt import methods
from os import abort
from urllib import response
from flask import Flask, jsonify, redirect, render_template, request, Response, Request, abort
import flask
from flask import url_for
from markupsafe import escape, Markup
import os 

app = Flask(__name__)


app.secret_key = b'as1d5a1f)(=/561)/(&hn'

# Llave que protege a los cockies
app.secret_key = os.urandom(16)

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

@app.route('/metodo/<metodow>', methods=['GET', 'POST'])
def metodow(metodow):
    return f'El metodo es {metodow}'
    
@app.route('/render')
def render():
    # De esta forma se pasan parametros al html
    # Es el arhivo y luego la calve y el valor 
    return render_template('index.html', valor=2)  


@app.route('/redireccion')
def redireccion():
    return redirect( url_for('metodow', metodow='GET'))

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error=error),404


# REST Representational state tranfer
@app.route('/api/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    # En este caso el jsonify no es necesario usarlo proque la respuesta es un 
    # diccionario
    return {"nombre":nombre, "metodo":request.method}

@app.route('/home/<usuario>')
def home(usuario):
    return render_template('home.html', usuario=usuario)

@app.route('/api/login')
def login2():
    usuario = 'Samuel'
    password = 123
    
    return redirect( url_for('home', usuario=usuario) )
    
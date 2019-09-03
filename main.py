from flask import Flask, escape, request, render_template
from Demo.db import init_db
from Demo.models import Gravacao

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
db_session = init_db()
    
@app.route('/gravacoes')
def gravacoes():
    """
    Aqui deve ser implementada a listagem de categorias de gravações
    """
    categorias = db_session.query(Gravacao).all()    

    render_template('gravacoes.html', categorias=categorias)
    
@app.route('/gravacoes/<categoria>')
def categoria(categoria):
    """
    Aqui deve ser implementada a listagem de gravações
    """
    categoria = None
    render_template('categoria.html', categoria=categoria)


@app.route('/autores')
def autores():
    """
    Aqui deve ser implementada a listagem de autores
    """
    autores = []
    render_template('autores.html', autores=autores)
    

@app.route('/autores/<slug>')
def autor(slug):
    """
    Aqui devem ser implementados os detalhes do autor
    """
    autores = []
    render_template('autor.html', autores=autores)
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')
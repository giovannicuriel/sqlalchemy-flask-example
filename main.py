from flask import Flask, escape, request, render_template
from Demo.db import init_db
from controller import get_all

app = Flask(__name__)
db_session = init_db()

@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/gravacoes')
def gravacoes():
    """
    Aqui deve ser implementada a listagem de categorias de gravações
    """
    categorias = []
    render_template('gravacoes.html', categorias=categorias)
    
@app.route('/gravacoes/<categoria>')
def categoria(categoria):
    """
    Aqui deve ser implementada a listagem de gravações
    """
    categoria = None
    render_template('categoria.html', categoria=categoria)


@app.route('/autores', methods=['GET', 'POST'])
def autores():
    if (request.method == 'POST'):
        insert(db_session, request.body)
    """
    Aqui deve ser implementada a listagem de autores
    """
    autores = get_all(db_session)
    return render_template('autores.html', autores=autores)
    

@app.route('/autores/<slug>')
def autor(slug):
    """
    Aqui devem ser implementados os detalhes do autor
    """
    autores = []
    render_template('autor.html', autores=autores)
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
"""
Este é um exemplo de uso do Flask, um microframework para desenvolvimento de
aplicações que tenham uma API HTTP.
"""

from flask import Flask
from flask import request, make_response
from Demo.controller import add_profile, get_profiles
from Demo.db import init_db
import json

"""
Esta é a aplicação principal do Flask
"""
app = Flask(__name__)
db_session = init_db()

"""
O registro de uma função para processamento de uma requisição é feito
adicionando-se uma anotação (o @ abaixo) referenciando a aplicação, endpoint e
o método (caso necessário) que a função será responsável por processar. No caso
abaixo, a função `process_profile_insertion` irá processar todas as requisições
de POST para o endpoint `/profiles`.

Uma coisa importante: os dados da requisição estará contida no objecto
`request` (que foi importado na linha 11 deste arquivo). Este objeto fornece
algumas funções úteis, como obter o objeto JSON da requisição sem necessidade
de processamento extra. O exemplo também imprime os cabeçalhos enviados na
requisição.

Ao final da função, a resposta retornada ao requerente (o elemento que gerou a
requisição) é montada com a função `make_response`.

Nota: em uma aplicação real, tome cuidado para não repassar as estruturas do
Flask para o seu componente. É muito fácil deixar isto acontecer, porém irá
aumentar muito a dependência da biblioteca com o seu componente, além de deixar
o código mais difícil de ser testado e documentado.

Outra coisa: repare a chamada da função `json.dumps`. Esta função transforma
um JSON em uma string, alterando qualquer caracter que venha a conflitar com
o padrão de descrição do JSON (por exemplo, aspas duplas). O inverso desta
função, isto é, transformar uma string em um JSON é a loads (para faciliar
a memorização, considere que `dumps` é um "dump string" e `loads` é um "load
string")
"""
@app.route('/profiles', methods=['POST'])
def process_profile_insertion():
    print('Inserted item: ' + json.dumps(request.json))
    print('Headers: ')
    for header in request.headers:
        print('{}'.format(header))
    add_profile(request.json, db_session)
    payload = json.dumps({"message": "ok!"})
    
    status = 200
    return make_response(payload, status)


"""
Esta função é responsável por processar GET no mesmo endpoint anterior. Como
nenhum índice é especificado, toda a lista armazenada até agora é incluída na
resposta.
"""
@app.route('/profiles', methods=['GET'])
def retrieve_list():
    print('Headers: ')
    for header in request.headers:
        print('{}'.format(header))
    profiles = get_profiles(db_session)
    payload = json.dumps({"message": "ok!", 'items': profiles})
    status = 200
    return make_response(payload, status)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

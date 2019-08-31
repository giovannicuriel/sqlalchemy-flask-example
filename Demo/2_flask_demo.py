"""
Este é um exemplo de uso do Flask, um microframework para desenvolvimento de
aplicações que tenham uma API HTTP.

Neste exemplo, iremos criar uma API simples que implementa a criação, leitura
e remoção de elementos em uma lista.

Como executar: 
Basta configurar a variável de ambiente FLASK_APP e chamar o módulo do Flask

.. code-block:: bash
   export FLASK_APP=./Demo/2_flask_demo.py
   python3 -m flask run

"""

from flask import Flask
from flask import request, make_response
import json
"""
Esta é a aplicação principal do Flask
"""
app = Flask(__name__)

inserted_list = []

"""
O registro de uma função para processamento de uma requisição é feito
adicionando-se uma anotação (o @ abaixo) referenciando a aplicação, endpoint e
o método (caso necessário) que a função será responsável por processar. No caso
abaixo, a função `process_list_insertion` irá processar todas as requisições de
POST para o endpoint `/list`.

Uma coisa importante: os dados da requisição estará contida no objecto `request`
(que foi importado na linha 11 deste arquivo). Este objeto fornece algumas funções
úteis, como obter o objeto JSON da requisição sem necessidade de processamento
extra. O exemplo também imprime os cabeçalhos enviados na requisição.

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
@app.route('/list', methods=['POST'])
def process_list_insertion():
    print('Inserted item: ' + json.dumps(request.json))
    print('Headers: ')
    for header in request.headers:
        print('{}'.format(header))
    payload = json.dumps({"message": "ok!"})
    inserted_list.append(request.json)
    status = 200
    return make_response(payload, status)


"""
Esta função é responsável por processar GET no mesmo endpoint anterior. Como
nenhum índice é especificado, toda a lista armazenada até agora é incluída na
resposta.
"""
@app.route('/list', methods=['GET'])
def retrieve_list():
    print('Headers: ')
    for header in request.headers:
        print('{}'.format(header))
    payload = json.dumps({"message": "ok!", 'items': inserted_list})
    status = 200
    return make_response(payload, status)

"""

Esta função é responsável pela recuperação de apenas um item desta lista.
Repare - e isto é importante - que a definição do endpoint contém um item
especial, o <ix>. Isto indica que a função que trata esta requisição terá um
parâmetro de mesmo nome (ix) que irá conter o valor passado no endpoint. Por
exemplo: uma requisição GET no endpoint /list/556 irá resultar na chamada desta
função com o parâmetro ix valendo 556.

Outra coisa importante: o tipo deste atributo é uma string. Para utilizar este
valor como sendo um índice de um vetor, deve-se converter esta variável para um
inteiro.
"""
@app.route('/list/<ix>', methods=['GET'])
def retrieve_list_item(ix):
    print('Headers: ')
    index = int(ix)
    for header in request.headers:
        print('{}'.format(header))
    if index >= len(inserted_list) or index < 0:
        status = 400
        payload = json.dumps({"message": "out of bound"})
    else:
        payload = json.dumps({"message": "ok!", 'items': inserted_list[int(index)]})
        status = 200
    return make_response(payload, status)

"""
Esta função tem o propósito semelhante da função anterior, diferenciando no fato
de que ela irá remover o valor passado como parâmetro.
"""
@app.route('/list/<ix>', methods=['DELETE'])
def remove_list_item(ix):
    print('Headers: ')
    index = int(ix)
    for header in request.headers:
        print('{}'.format(header))
    if index >= len(inserted_list) or index < 0:
        status = 400
        payload = json.dumps({"message": "out of bound"})
    else:
        # Remove o item selecionado
        item = inserted_list[index]
        del inserted_list[index]
        payload = json.dumps({"message": "ok!", 'removed_item': item})
        status = 200
    return make_response(payload, status)


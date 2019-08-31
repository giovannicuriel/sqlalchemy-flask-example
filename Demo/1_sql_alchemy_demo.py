# -*- coding: utf-8 -*-
"""
Olá! Esta é uma demonstração do SQLAlchemy. Em poucas palavras, o SQLAlchemy
é uma biblioteca para ORM que suporta vários bancos de dados.

O que é ORM? - você pode perguntar: não tema! ORM significa *Object-Relational Mapping*.
De acordo com o Wikipedia:

..
   [ORM] é uma técnica de programaçõ apra conversão de dados entre sistemas
   tipados incompatíveis usando linguagens de programação orientadas a objeto.

Como se pode concluir, ela é bastante apropriada para acessos a banco de dados.
Ao invés de escrever instruções de SQL longas e complexas, além de várias
linhas de código apenas para obter dados de uma tabela em particular (o que
incluiria não somente as instruções SQL mas também verificação de nomes de
colunas e tipos de dados, incluindo as suas relações com outras tabelas), quel
tal criar um objeto Python e inseri-lo diretamente no banco de dados? Um
exemplo:

.. code-block::python

    obj = Person(name='Jon', surname='Doe', age=25)
    session = db.Session()
    session.add(obj)
    session.commit()

Sem aporrinhações, sem códigos extras, sem chamadas específicas para o banco de
dados, apenas mágica.

Neste tutorial, nós construiremos um serviço de gerenciamento de perfis de
usuários bastante simples, apenas para mostrar e validar algumas
funcionalidades básicas do SQLAlchemy.

"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

"""
Antes de mais nada: embora o SQLAlchemy possua propriedades mágicas e exponha
uma API interessante e fácil de usar para modelamento de entidades, ele necessita
acessar um banco de dados. Esta chamada criará uma instância do SQLite em memória.
Caso outro banco de dados seja necessário, ela poderia ser referenciada aqui
através de uma URI apropriada, como `mysql://antonio:superpasswd@server/table`.
"""
database_engine = create_engine('sqlite:///:memory:')

"""
Esta `declarative_base` cria uma classe base para a definição de modelos. Ela
é a razão pela qual é possível declarar atributos de classes que são mapeadas
diretamente em colunas em tabelas.
"""
Base = declarative_base()
 
"""
Aqui definimos a nossa classe. Ela é associada a uma tabela através do atributo
`__tablename__`.
"""
class UserProfile(Base):
    __tablename__ = "UserProfiles"
 
    Id = Column(Integer, primary_key=True)
    Name = Column(String)  
    Surname = Column(String)
    Age = Column(Integer)

"""
Por fim, a amarração entre a definição do modelo de dados e o banco de dados.
O atributo `bind`, configurado abaixo, indica à classe base que criamos
anteriormente qual deve ser o banco de dados a ser utilizado. A chamada `create_all()`
é quase autoexplicativa: ela envia comandos ao banco de dados para a criação de
todos os recursos necessários para que os dados definidos nas classes derivadas
de `Base` possam ser armazenados corretamente.
"""
Base.metadata.bind = database_engine        
Base.metadata.create_all()


"""
Aqui iniciamos o uso das coisas que criamos e configuramos anteriormente.
A sessão serve para armazenar todas as operações necessárias no banco de dados,
como inserção e remoção de itens.
"""        
Session = sessionmaker(bind=database_engine)
db_session = Session()

"""
Para usá-la, basta chamar uma de suas funções fornecidas pela API. Por exemplo,
a função `add_all` recebe uma lista de objetos (repare que os objetos são construídos
na definição desta lista) que derivam de `Base`. Note que estes objetos não possuem
nenhuma característica especial além de serem classes filhas de `Base`.
"""
db_session.add_all(
   [
       UserProfile(Name="Jon", Surname="Doe", Age=10),
       UserProfile(Name="Linda", Surname="Witherfork", Age=34),
   ])

"""
Para executar todas as operações pendentes, devemos chamar a função `commit()`.
"""
db_session.commit()

"""
E é isso.
Vamos ler todas as informações armazenadas até agora.
Repare que o parâmetro passado para a função `query` é o nome da classe associada
aos itens que desejamos obter. O SQLAlchemy identifica qual tabela ele deve
pesquisar e criar uma lista de objetos contendo os dados que foram mapeados na
classe.
"""

query_results = db_session.query(UserProfile).all()

for profile in query_results:
    print(f"{profile.Surname}, {profile.Name}: {profile.Age}")

"""
E como posso executar?

Simples. Como este projeto utiliza pipenv, basta executar.

.. code-block::bash
   pipenv install # instala todas as dependências
   pipenv run python3 Demo/1_sql_alchemy_demo.py # Executa a demonstração

"""
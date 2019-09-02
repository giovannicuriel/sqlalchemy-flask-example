from Demo.models import UserProfile

def get_profiles(session):
    '''
    Obtém a lista de perfis configurada
    
    Vamos ler todas as informações armazenadas até agora.
    Repare que o parâmetro passado para a função `query` é o nome da classe
    associada aos itens que desejamos obter. O SQLAlchemy identifica qual tabela
    ele deve pesquisar e criar uma lista de objetos contendo os dados que foram
    mapeados na classe.
    '''
    query_results = session.query(UserProfile).all()
    results = []

    for profile in query_results:
        print(f'{profile.LastName}, {profile.Name}: {profile.Age}')
        results.append(profile.to_dict())
    return results

def add_profile(profile, session):
    '''
    Adiciona um perfil no banco de dados
    Para usá-la, basta chamar uma de suas funções fornecidas pela API. Por exemplo,
    a função `add_all` recebe uma lista de objetos (repare que os objetos são
    construídos na definição desta lista) que derivam de `Base`. Note que estes
    objetos não possuem nenhuma característica especial além de serem classes
    filhas de `Base`.
    '''
    session.add(UserProfile(**profile))

    '''
    Para executar todas as operações pendentes, devemos chamar a função `commit()`.
    '''
    session.commit()

    '''
    E é isso.
    '''

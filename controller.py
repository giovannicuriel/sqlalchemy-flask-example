from models import Author

def get_all(session):
    authors = session.query(Author).all()
    results = []
    for author in authors:
        results.append(author.to_dict())
    return results

def insert(session, data):
    session.add(Author(**data))
    session.commit()
    return 'Foi'

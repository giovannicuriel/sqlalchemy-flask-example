
from sqlalchemy import Column, Integer, String
from Demo.db import Base

"""
Aqui definimos a nossa classe do perfil do usuário. Ela é associada a uma
tabela através do atributo `__tablename__`.

Repare que a classe Base é importada do módulo `db`.
"""

class UserProfile(Base):
    __tablename__ = "UserProfiles"
 
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)  
    LastName = Column(String)
    Age = Column(Integer)

    def to_dict(self):
        return {
            "Id": self.Id,
            "Name": self.Name,
            "LastName": self.LastName,
            "Age": self.Age
        }

class Gravacao(Base):
    __tablename__ = "Gravacoes"
 
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Link = Column(String)
    Categoria = Column(String)
    Nome = Column(String)  

    def to_dict(self):
        return {
            "Id": self.Id,
            "Link": self.Link,
            "Categoria": self.Categoria,
            "Nome": self.Nome
        }

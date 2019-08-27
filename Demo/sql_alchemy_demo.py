# -*- coding: utf-8 -*-
"""
Hi, this is a SQLAlchemy demo. In a nutshell, SQLAlchemy is a ORM library that
supports many databases.

What is ORM? - you might ask. Fear not: ORM stands for Object-Relational-Mapping.
As stated in Wikipedia:

..
   [ORM] is a programming technique for converting data between incompatible
   type systems using object-oriented programming languages.

As you'd might think, this is perfectly suitable for database access. Instead
of writing long, complex SQL statements and many lines of code just to retrieve
data from a particular table (which include not only the SQL statement itself,
but also checking column names and data types, incluing their relationships to
other tables), how about create a Python object and inserting it as is into a
database? I mean:

.. code-block::python

    obj = Person(name='Jon', surname='Doe', age=25)
    session = db.Session()
    session.add(obj)
    session.commit()

No hassle, no extra code, no database-specific calls, just magic.

In this tutorial, we'll build a user profile management service.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

"""
First things first: although SQLAlchemy has magical properties and offers a
very nice and easy to use interface for modelling entities, it needs a
database. This call will use a SQLite instance in-memory. If other database
instance is needed, you could set where it can be accessed, just as
`mysql://jondoe:superpasswd@server/table`.
"""
database_engine = create_engine('sqlite:///:memory:')

"""
This `declarative_base` creates a base class for model definitions. It is the
reason why we can declare class attributes directly mapped onto table columns.
"""
Base = declarative_base()
 

"""
And here we define our class. It is associated to a table by setting the
`__tablename__` attribute.
"""
class UserProfile(Base):
    __tablename__ = "UserProfiles"
 
    Id = Column(Integer, primary_key=True)
    Name = Column(String)  
    Surname = Column(String)
    Age = Column(Integer)

"""
Here we finish the configuration part. It will associate the SQLite engine we
created previously and call `create_all`, which will send all commands (probably
SQL statements) to the database engine in order to create all resources needed
by our application (which is defined by all model classes derived from `Base`).
"""
Base.metadata.bind = database_engine        
Base.metadata.create_all()


"""
In order to do things using the database, we need to create a session.
We will use db_session whenever we need to retrieve, save, filter or otherwise
access the database.
"""        
Session = sessionmaker(bind=database_engine)
db_session = Session()

"""
To use it, it offers a nice API with well documented operations. For instace,
let's add two profiles into the database. To do that, we just create two objects
from `UserProfile` class. Remember that these objects have nothing special but
being derived from `Base` class.
"""
db_session.add_all(
   [
       UserProfile(Name="Jon", Surname="Doe", Age=10),
       UserProfile(Name="Linda", Surname="Witherfork", Age=34),
   ])

"""
To execute all pending operations associated to the database session, we need
to call `commit()` function
"""
db_session.commit()

"""
And that's it.
Let's retrieve all Profile objects from the database.
"""

query_results = db_session.query(UserProfile).all()

for profile in query_results:
    print(f"{profile.Surname}, {profile.Name}: {profile.Age}")
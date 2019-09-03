from sqlalchemy import Column, Integer, String
from Demo.db import Base

class Author(Base):
    __tablename__ = "AuthorProfile"
 
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)
    Description = Column(String)
    Url = Column(String)
    Slug = Column(String)

    def to_dict(self):
        return {
            "Id": self.Id,
            "Name": self.Name,
            "Description": self.Description,
            "Url": self.Url,
            "Slug": self.Slug,
        }


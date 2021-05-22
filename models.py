import db
from sqlalchemy import Column, Integer, String
class Contact(db.Base):
    __tablename__ = "contact"
    name = Column(Integer)
    email = Column(String, primary_key=True)
    phone = Column(String)
    
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    
    def __str__(self):
        return f"{self.name}: {self.phone}"
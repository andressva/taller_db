import db
from models import *

class Agend():
  
  def save_contact(contact):
    ctc = Contact(contact['name'], contact['email'], contact['phone'])
    db.session.add(ctc)
    db.session.commit()
  
  def get_contacts():
    contacts = []
    contacts_query = db.session.query(Contact).all()
    for c in contacts_query:
      contacts.append({'name': c.name, 'email': c.email, 'phone': c.phone})
    
    return contacts

  def delete_contact(name):
    db.session.query(Contact).filter(Contact.name==name).delete()
    db.session.commit()
  
  def edit_contact(new_name, name, new_email, email, new_phone, phone):
    db.session.query(Contact)\
       .filter(Contact.email == email)\
       .update({Contact.name: new_name, Contact.email: new_email, Contact.phone: new_phone})
    db.session.commit()
        
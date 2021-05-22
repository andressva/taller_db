from tkinter import *
from tkinter import ttk
from sqlalchemy.sql.expression import column
from agend import *
class AgendApp(Frame):
  
  def __init__(self, window):
    self.wind = window
    self.wind.title("Agenda Telefonica")
    self.wind.resizable(False, False)
    
    self.name = StringVar()
    self.email = StringVar()
    self.phone = StringVar()
    
    frame = LabelFrame( self.wind, text = "Registrar Contacto:")
    frame.grid(row=0, column=0, columnspan=3)
    
    Label(frame, text = "Nombre").grid(row=1,column=0)
    self.nameEntry = Entry(frame, textvariable=self.name)
    self.nameEntry.grid(row=1, column=1)
    
    Label(frame, text = "Correo").grid(row=2,column=0)
    self.emailEntry = Entry(frame, textvariable=self.email)
    self.emailEntry.grid(row=2, column=1)
    
    Label(frame, text = "Telefono").grid(row=3,column=0)
    self.phoneEntry = Entry(frame, textvariable=self.phone)
    self.phoneEntry.grid(row=3, column=1)
    
    Label(frame, text = "").grid(row=5,column=0)
    Label(frame, text = "").grid(row=7,column=0)
    
    Button(frame, text="GUARDAR", command=self.save_contact, bg="#3498db",fg="white", padx=10, pady=5).grid(row=6,column=0, columnspan=3)
    
    
    self.msg = Label(text = '', fg = '#c0392b')
    self.msg.grid(row=3, column=0, columnspan=3, sticky= W + E)

    self.tree = ttk.Treeview(height = 10, columns = (0, 1, 2), show="headings")
    self.tree.grid(row=4, column=0, columnspan=3)

    self.tree.heading(0, text = 'Nombre', anchor = CENTER)
    self.tree.heading(1, text = 'Email', anchor = CENTER)
    self.tree.heading(2, text = 'Telefono', anchor = CENTER)
    
    self.list_contacts()
    
    Button(text="ELIMINAR", command=self.delete_contact, bg="#e74c3c",fg="white").grid(row=5,column=0, sticky=W + E)
    Button(text="EDITAR", command=self.edit_contact, bg="#f1c40f",fg="white").grid(row=5,column=1, sticky=W + E)
  
  def save_contact(self):
    if self.validate_save() :
      data = {
        'name': self.name.get(),
        'email': self.email.get(),
        'phone': self.phone.get()
      }
      Agend.save_contact(data)
      self.list_contacts()
      self.msg['text'] = f'Contacto {self.name.get()}, guardado!'
      self.reset_inputs()
    else:
      self.msg['text'] = 'Nombre, Email y/o Telefono requerido!'
  
  def list_contacts(self):
    self.clean_table()
    contacts = Agend.get_contacts()
    for c in contacts:
      self.tree.insert('', 0, text = c['name'], values=(c['name'], c['email'], c['phone']))
  
  def delete_contact(self):
    self.msg['text'] = ''
    try:
        self.tree.item(self.tree.selection())['values'][0]
    except:
        self.msg['text'] = '¡Por favor selecciona un contacto!'
        return
    name = self.tree.item(self.tree.selection())['text']
    Agend.delete_contact(name)
    self.list_contacts()
  
  def edit_contact(self):
      self.msg['text'] = ''
      try:
          self.tree.item(self.tree.selection())['values'][0]
      except:
          self.msg['text'] = '¡Por favor selecciona un contacto!'
          return
      name = self.tree.item(self.tree.selection())['values'][0]
      _email = self.tree.item(self.tree.selection())['values'][1]
      _phone = self.tree.item(self.tree.selection())['values'][2]
      self.edit_wind = Toplevel()
      Label(self.edit_wind, text = 'Nombre:').grid(row = 0, column = 1)
      Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = name), state = 'readonly').grid(row = 0, column = 2)
      
      Label(self.edit_wind, text = 'Nuevo Nombre:').grid(row = 1, column = 1)
      new_name = Entry(self.edit_wind)
      new_name.grid(row = 1, column = 2)

    
      Label(self.edit_wind, text = 'Email:').grid(row = 2, column = 1)
      Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = _email), state = 'readonly').grid(row = 2, column = 2)
   
      Label(self.edit_wind, text = 'Nuevo Email:').grid(row = 3, column = 1)
      new_email= Entry(self.edit_wind)
      new_email.grid(row = 3, column = 2)
      
      Label(self.edit_wind, text = 'Telefono:').grid(row = 4, column = 1)
      Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = _phone), state = 'readonly').grid(row = 4, column = 2)
   
      Label(self.edit_wind, text = 'Nuevo Telefono:').grid(row = 5, column = 1)
      new_phone= Entry(self.edit_wind)
      new_phone.grid(row = 5, column = 2)

      Button(self.edit_wind, text = 'Actualizar', command = lambda:self.handle_edit(new_name.get(), name, new_email.get(), _email, new_phone.get(), _phone)).grid(row = 6, column = 2, sticky = W)
      self.edit_wind.mainloop()
  
  def handle_edit(self, new_name, name, new_email, email, new_phone, phone):
    Agend.edit_contact(new_name, name, new_email, email, new_phone, phone)
    self.edit_wind.destroy()
    self.msg['text'] = 'Contacto actualizado!'
    self.list_contacts()
  
  def validate_save(self):
    return len(self.name.get()) != 0 and  ( len(self.email.get()) != 0 or len(self.phone.get()) != 0 )  
    
  def reset_inputs(self):
    self.name.set('')
    self.email.set('')
    self.phone.set('')
  
  def clean_table(self):
    records = self.tree.get_children()
    for e in records:
      self.tree.delete(e)
        
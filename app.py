from tkinter import *

class AgendApp(Frame):
  
  def __init__(self, window):
    self.wind = window
    self.wind.title = "Agenda Telefonica"
    self.wind.geometry("700x500")
    
    self.name = StringVar()
    self.email = StringVar()
    self.phone = StringVar()
    
    frame = LabelFrame( self.wind, text = "Registrar Contacto:")
    frame.grid(row=0, column=0, columnspan=3, pady=20)
    
    Label(frame, text = "Nombre").grid(row=1,column=0)
    self.nameEntry = Entry(frame, textvariable=self.name)
    self.nameEntry.grid(row=1, column=1)
    
    Label(frame, text = "Correo").grid(row=2,column=0)
    self.emailEntry = Entry(frame, textvariable=self.email)
    self.emailEntry.grid(row=2, column=1)
    
    Label(frame, text = "Telefono").grid(row=3,column=0)
    self.phoneEntry = Entry(frame, textvariable=self.phone)
    self.phoneEntry.grid(row=3, column=1)
    
    Button(frame, text="Guardar", command=self.save_contact, bg="#009",fg="white").grid(row=5,column=0)
  
  
  def save_contact(self):
    print('Saving...')
    print(self.name.get())
    print(self.email.get())
    print(self.phone.get())
        
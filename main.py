"""
TALLER #7
Aplicacion con base de datos

INTEGRANTES:
Alvaro Jose Vergara
Andres Vergel Alvarez
Eddie Enrique Yanez
Jhonys Orozco
"""


from tkinter import *
from app import *
import db

if __name__ == '__main__':
  window = Tk()
  view = AgendApp(window)
  window.mainloop()
  db.Base.metadata.create_all(db.engine)
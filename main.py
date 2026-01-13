from tkinter import *
import sqlite3

#Conecta com o banco e instanciona o Cursor
conection = sqlite3.connect("banco.db")
cursor = conection.Cursor()

#criação e configuração da telaPrincipal
telaPrincipal = Tk()
telaPrincipal.title("Crud")
telaPrincipal.config(height=616,width=1066)


telaPrincipal.mainloop()
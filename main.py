from tkinter import *
import sqlite3

#Conecta com o banco e instanciona o Cursor
conection = sqlite3.connect("banco.db")
cursor = conection.cursor()
#Cria a tabela para registrar as compras                      cliente -> funcionário
cursor.execute("""CREATE TABLE IF NOT EXISTS compras(
               Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               Data TEXT NOT NULL,
               Cliente TEXT NOT NULL,
               ValorDaCompra FLOAT NOT NULL
               )""")
conection.commit()


#criação e configuração da telaPrincipal
telaInicial = Tk()
telaInicial.title("Crud")
telaInicial.config(height=616,width=1066)


telaInicial.mainloop()
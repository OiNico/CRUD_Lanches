from tkinter import *
import sqlite3

#Conecta com o banco e instanciona o Cursor
conection = sqlite3.connect("banco.db")
cursor = conection.cursor()

#Cria a tabela de produtos
cursor.execute("""CREATE TABLE IF NOT EXISTS produtos(
               Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               Descricao TEXT NOT NULL,
               Preco FLOAT NOT NULL,
               IdCategoria INTEGER,
               Imagem BLOB
               )""")

#Cria a tabela de categorias dos produtos
cursor.execute("""CREATE TABLE IF NOT EXISTS categorias(
               Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               Descricao TEXT NOT NULL
               )""")

#Cria a tabela para registrar as compras                      cliente -> funcionário
cursor.execute("""CREATE TABLE IF NOT EXISTS vendas(
               Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               Data TEXT NOT NULL,
               Cliente TEXT NOT NULL,
               ValorDaVenda FLOAT NOT NULL
               )""")
conection.commit()
conection.close()

#criação e configuração da telaPrincipal
telaInicial = Tk()
telaInicial.title("Crud")
telaInicial.config(height=616,width=1066)


telaInicial.mainloop()
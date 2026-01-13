import tkinter as tk
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

#Cria a tabela para registrar as compras
cursor.execute("""CREATE TABLE IF NOT EXISTS vendas(
               Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               Data TEXT NOT NULL,
               Cliente TEXT NOT NULL,
               ValorDaVenda FLOAT NOT NULL
               )""")
conection.commit()
conection.close()

#criação e configuração da Janela
Janela = tk.Tk()
Janela.geometry("1066x616")
Janela.title("Crud Lanches")

#configuração do texto de bem vindo e do botão para ir para a tela de Cadastro
telaInicial = tk.Frame(Janela)
telaInicial.pack(fill="both", expand= True)

def IrTelaCadastro():
    telaInicial.pack_forget()
    TelaCadastro.pack()

tk.Label(telaInicial, text="Bem vindo ao Sistema de Lanches", height=10, width=100).pack()
tk.Button(telaInicial, text="Cadastrar", command=IrTelaCadastro).pack()

#configuração da tela de cadastro
TelaCadastro = tk.Frame()
tk.Label(TelaCadastro, text="Tela de cadastro").pack(side="left")

Janela.mainloop()
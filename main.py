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

# Faz o grid ocupar todo o frame - by ChatGPT
telaInicial.columnconfigure(1, weight=1)
telaInicial.rowconfigure(0, weight=1)
telaInicial.rowconfigure(1, weight=1)
telaInicial.rowconfigure(2, weight=1)

def IrTelaCadastro():
    telaInicial.pack_forget()
    TelaCadastro.pack(fill="both", expand=True)
def IrTelaInicial():
    TelaCadastro.pack_forget()
    telaInicial.pack(fill="both",expand=True)

tk.Label(telaInicial, text="Bem vindo ao Sistema de Lanches").grid(row=0,column=0,padx=5,pady=5, sticky="n")
tk.Button(telaInicial, text="Cadastrar", command=IrTelaCadastro).grid(row=10,column=10,padx=10, pady=10, sticky="e")

#configuração da tela de cadastro
TelaCadastro = tk.Frame()
tk.Label(TelaCadastro, text="Tela de cadastro").grid(row=0,column=0,padx=5,pady=5, sticky="n")
tk.Button(TelaCadastro, text="Voltar", command=IrTelaInicial).grid(row=10,column=10,padx=10, pady=10, sticky="e")

# Faz o grid ocupar todo o frame - by ChatGPT
TelaCadastro.columnconfigure(1, weight=1)
TelaCadastro.rowconfigure(0, weight=1)
TelaCadastro.rowconfigure(1, weight=1)
TelaCadastro.rowconfigure(2, weight=1)

Janela.mainloop()
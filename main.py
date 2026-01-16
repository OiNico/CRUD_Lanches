import tkinter as tk
import sqlite3
from classes import *

class BancoDb:
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
#criação das outras telas
TelaCadastroItens = tk.Frame()
TelaCriarCategorias = tk.Frame()
TelaCadastro = tk.Frame()

def LimparEntry(tela):
    for widget in tela.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)

def IrTelaCadastro():
    telaInicial.pack_forget()
    LimparEntry(telaInicial)
    TelaCadastro.pack(fill="both", expand=True)
def IrTelaInicial():
    TelaCadastro.pack_forget()
    TelaCadastroItens.pack_forget()
    TelaCriarCategorias.pack_forget()
    LimparEntry(telaInicial)
    telaInicial.pack(fill="both",expand=True)
def IrTelaCadastroItens():
    telaInicial.pack_forget()
    TelaCadastroItens.pack(fill="both", expand=True)
def IrTelaCriarCategorias():
    telaInicial.pack_forget()
    TelaCriarCategorias.pack(fill="both", expand=True)

tk.Label(telaInicial, text="Bem vindo ao Sistema de Lanches").grid(row=0,column=0,padx=5,pady=5, sticky="w")

#IrTelaCadastro botão
tk.Button(telaInicial, text="Cadastrar Cliente", command=IrTelaCadastro).grid(row=5,column=10,padx=5, pady=5, sticky="s")

#IrTelaCadastroItens botão * organizar as telas
tk.Button(telaInicial, text="Visualizar itens", command=IrTelaCadastroItens).grid(row=5,column=9,padx=5,pady=5,sticky="s")

#IrTelaCriarCategorias botão
tk.Button(telaInicial, text="Visualizar Categoria", command=IrTelaCadastroItens).grid(row=5,column=8,padx=5,pady=5,sticky="s")

#configuração da tela de cadastro
tk.Label(TelaCadastro, text="Tela de cadastro").grid(row=0,column=0,padx=2,pady=2, sticky="nw", columnspan=2)

#IrTelaInicial botão
tk.Button(TelaCadastro, text="Voltar", command=IrTelaInicial).grid(row=10,column=0,padx=5, pady=10, sticky="w", columnspan=10)

#entrada do nome do cliente
nomeUsuario = tk.Entry(TelaCadastro, width=35)
nomeUsuario.grid(row=5,column=1,sticky="w", padx=5, columnspan=2)
tittleNomeUsuario = tk.Label(TelaCadastro, text="Insira seu nome: ")
tittleNomeUsuario.grid(row=5,column=0, sticky="w", padx=5, columnspan=2)

#entrada senha
senhaUsuario = tk.Entry(TelaCadastro, width=35, show="*")
senhaUsuario.grid(row=7,column=1, sticky="w", padx= 5)
tittleSenhaUsuario = tk.Label(TelaCadastro, text="Insira sua senha: ")
tittleSenhaUsuario.grid(row=7,column=0,sticky="w")

# Faz o grid ocupar todo o frame - by ChatGPT
telaInicial.columnconfigure(0, weight=1)

#Configuração tela de cadastro de itens e de categorias

#Criar categoria, precisa somente da descrição

#informações p/ criar um item: Descrição, preço, Idcategoria, imagem(binária)

#IrTelaInicial Botão
tk.Button(TelaCadastroItens, text="Voltar", command=IrTelaInicial).grid(row=10,column=0,padx=5, pady=10, sticky="w", columnspan=10)
tk.Button(TelaCriarCategorias, text="Voltar", command=IrTelaInicial).grid(row=10,column=0,padx=5, sticky="w")

Janela.mainloop()
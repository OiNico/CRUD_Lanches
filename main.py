import tkinter as tk
import sqlite3
from itemCARA import Categoria


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

    def SelectCategorias():
        conection = sqlite3.connect("banco.db")
        cursor = conection.cursor()

        cursor.execute("""SELECT Descricao FROM categorias""")
        categorias = cursor.fetchall()

        return categorias

    conection.close()


#criação e configuração da Janela
Janela = tk.Tk()
Janela.geometry("1066x616")
Janela.title("Crud Lanches")
Janela.resizable(width=False,height=False)

#configuração do texto de bem vindo e do botão para ir para a tela de Cadastro
telaInicial = tk.Frame(Janela)
telaInicial.pack(fill="both", expand= True)
#criação das outras telas
TelaCadastroItens = tk.Frame()
TelaCriarCategorias = tk.Frame()

def LimparEntry(tela):
    for widget in tela.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)

def IrTelaInicial():
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

#IrTelaCadastroItens botão * organizar as telas
tk.Button(telaInicial, text="Visualizar itens", command=IrTelaCadastroItens).grid(row=5,column=9,padx=5,pady=5,sticky="s")

#IrTelaCriarCategorias botão
tk.Button(telaInicial, text="Visualizar Categorias", command=IrTelaCadastroItens).grid(row=5,column=8,padx=5,pady=5,sticky="s")

# Faz o grid ocupar todo o frame - by ChatGPT
telaInicial.columnconfigure(0, weight=1)

#Configuração tela de cadastro de itens e de categorias

#Criar categoria, precisa somente da descrição
listBOX = tk.Listbox(TelaCriarCategorias, width=100,height=100)
listBOX.grid(row=0, column=0,padx=5,pady=5,sticky="w")

CarregarLISTAcategorias = Categoria.CarregarListBOX()

tk.Button(TelaCriarCategorias, text="Carregar Categorias", command=CarregarLISTAcategorias).grid(row=10,column=1,padx=5,sticky="w")

#informações p/ criar um item: Descrição, preço, Idcategoria, imagem(binária)

#IrTelaInicial Botão
tk.Button(TelaCadastroItens, text="Voltar", command=IrTelaInicial).grid(row=10,column=0,padx=5, pady=10, sticky="w", columnspan=10)
tk.Button(TelaCriarCategorias, text="Voltar", command=IrTelaInicial).grid(row=10,column=0,padx=5, sticky="w")

if __name__ == "__main__":
    Janela.mainloop()
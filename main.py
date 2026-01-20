import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import ttk

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
    def CriarCategoria():
        descricao = descricaoCATEGORIA.get()
        conection = sqlite3.connect("banco.db")
        cursor = conection.cursor()
        
        cursor.execute("""INSERT INTO categorias
                                (Descricao) VALUES
                                (?)""", (descricao,))
        
        conection.commit()
        conection.close()
    
    def LimparCategoria():
        conection = sqlite3.connect("banco.db")
        cursor = conection.cursor()
        
        if messagebox.askyesno("Confirmação", "Deseja realmente apagar a última categoria criada?"):
            cursor.execute("""DELETE FROM categorias
                       where Id = (
                            SELECT Id FROM categorias
                            ORDER BY Id DESC
                            LIMIT 1)""")
        

        conection.commit()
        conection.close()
    def RecarregarCategoria():
        VIEWcategorias.delete(0, tk.END)
        
        categoriasEXISTENTES = BancoDb.SelectCategorias()
        
        for c in categoriasEXISTENTES:
            VIEWcategorias.insert(tk.END, c[0])

    conection.close()


#criação e configuração da Janela
Janela = tk.Tk()
Janela.geometry("1066x616")
Janela.title("Crud Lanches")
Janela.resizable(width=False,height=False)

#centraliza a tela
Janela.update_idletasks()
x = (Janela.winfo_screenwidth() - Janela.winfo_width())//2
y = (Janela.winfo_screenheight() - Janela.winfo_height())//2
Janela.geometry(f"+{x}+{y}")

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
tk.Button(telaInicial, text="Visualizar Categorias", command=IrTelaCriarCategorias).grid(row=5,column=8,padx=5,pady=5,sticky="s")

# Faz o grid ocupar todo o frame - by ChatGPT
telaInicial.columnconfigure(0, weight=1)

#Configuração tela de cadastro de itens e de categorias

#Criar categoria, precisa somente da descrição
VIEWcategorias = tk.Listbox(TelaCriarCategorias, width=82, height=20)
VIEWcategorias.grid(row=0,column=0, sticky="nw", rowspan=2, padx= 5, pady=5)

descricaoCATEGORIA = tk.Entry(TelaCriarCategorias, width=20)
descricaoCATEGORIA.grid(row=6, column=0, sticky="w", padx=10)

btnCriarCategoria = tk.Button(TelaCriarCategorias, text="Criar Categoria", command=BancoDb.CriarCategoria)
btnCriarCategoria.grid(row=6, column=0,sticky="w", padx=140)

btnExcluirCategoria = tk.Button(TelaCriarCategorias, text="Excluir Última Categoria", command=BancoDb.LimparCategoria)
btnExcluirCategoria.grid(row=7, column=0, sticky="w", padx=125)

btnRecarregar = tk.Button(TelaCriarCategorias, text="Recarregar", command=BancoDb.RecarregarCategoria)
btnRecarregar.grid(row=7, column=0, sticky="w", padx= 55)

#CATEGORIAS -> Inicio
VOLTARcategorias = tk.Button(TelaCriarCategorias, text="Voltar", command=IrTelaInicial)
VOLTARcategorias.grid(row=7,column=0, sticky="w", padx=10)

#informações p/ criar um item: Descrição, preço, Idcategoria, imagem(binária)

#ITENS -> Inicio
VOLTARitens = tk.Button(TelaCadastroItens, text="AAA", command=IrTelaInicial)
VOLTARitens.grid(row=10,column=0,sticky="s", columnspan=10)

if __name__ == "__main__":
    Janela.mainloop()
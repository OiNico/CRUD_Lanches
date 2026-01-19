import sqlite3
from main import BancoDb
import tkinter as tk

class item:
    print("classe base de itens")

class categoria:

    def CriarCategoria(descricao):
        BancoDb.cursor.execute("""INSERT INTO categorias
                               (Id, Descricao) VALUES
                               (  , {})""", descricao)
        
    
    def CarregarListBox(listBOX):
        listBOX.delete(0, tk.END)
        categorias = BancoDb.SelectCategorias()

        for categoria in categorias:
            listBOX.insert(tk.END, categorias[0])
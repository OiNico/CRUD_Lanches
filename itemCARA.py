import sqlite3
from main import BancoDb

class CategoriaCARA:

    def CarregarListBox(listBOX):
        listBOX.delete(0)
        categorias = BancoDb.SelectCategorias()

        for categoria in categorias:
            listBOX.insert( categorias[0])
import sqlite3
from main import BancoDb

class item:
    print("classe base de itens")

class categoria:

    def CriarCategoria(descricao):
        BancoDb.cursor.execute("""INSERT INTO categorias
                               (Id, Descricao) VALUES
                               (  , {})""", descricao)
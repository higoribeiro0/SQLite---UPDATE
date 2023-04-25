import sqlite3 
from sqlite3 import Error

###Criar conexao
def ConexaoBanco():
    caminho="D:\\Python\\Aulas\\Banco\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

#####Criar tabela
#vsql="""CREATE TABLE tb_contatos(
#            N_IDCONTATO INTEGER PRIMARY KEY AUTOIMCREMENT,
#            T_NOMECONTATO VARCHAR(30),
#            T_TELEFONECONTATO VARCHAR(14),
#            T_EMAILCONTATO VARCHAR(30)
#        );"""

#UPDATE - Atualizar(SET)
def atualizar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro atualizado")
vsql="UPDATE tb_contatos SET T_NOMECONTATO='Higo' WHERE N_IDCONTATO=1"

atualizar(vcon,vsql)
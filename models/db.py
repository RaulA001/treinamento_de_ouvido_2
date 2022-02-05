from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.column('id', db.Integer, primary_key=True, autoincrement=True)
    id_notas = db.column('id', db.Integer, primary_key=True, autoincrement=True)
    id_testes = db.column('id', db.Integer, primary_key=True, autoincrement=True)
    volume = db.column(db.Integer)

    #def __init__(self):

class Testes(db.Model):

    id = db.column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.column(db.String)
    id_notas = db.column('id', db.Integer, primary_key=True, autoincrement=True)
    n_pergunta = db.column(db.Integer)
    pontos = db.column(db.Integer)
    duracao = db.column(db.DateTime)


    #def __init__(self):

class Testando(db.Model):

    id = db.column('id', db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.column('id', db.Integer, primary_key=True, autoincrement=True)
    id_teste = db.column('id', db.Integer, primary_key=True, autoincrement=True)
    pontos = db.column(db.Integer)

    #def __init__(self):


class Notas(db.Model):

    id = db.column('id', db.Integer, primary_key=True, autoincrement=True)
    nome_grermanica = db.column(db.String)
    nome_grego = db.column(db.String)
    oitavas = db.column(db.Integer)
    tipo = db.column(db.String)
    tipo_do_arquivo = db.column(db.String)
    pasta = db.column(db.String)

    #def __init__(self):


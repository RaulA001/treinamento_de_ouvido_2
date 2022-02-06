from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Testes(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    n_pergunta = db.Column(db.Integer)
    pontos = db.Column(db.Integer)
    duracao = db.Column(db.DateTime)
    testes_id = db.Column(db.Integer, db.ForeignKey('testando.id'))


    def __init__(self, nome=nome, n_pergunta=n_pergunta, pontos=pontos, duracao=duracao):
        self.Nome = nome
        self.n_pergunta = n_pergunta
        self.pontos = pontos
        self.duracao = duracao

class Testando(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pontos = db.Column(db.Integer)
    notas_id = db.relationship('Notas', backref='testando')
    testes_id = db.relationship('Testes', backref='testando')

    def __init__(self, pontos=pontos):
       self.pontos = pontos


class Notas(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_grermanica = db.Column(db.String)
    nome_grego = db.Column(db.String)
    oitavas = db.Column(db.Integer)
    tipo = db.Column(db.String)
    tipo_do_arquivo = db.Column(db.String)
    pasta = db.Column(db.String)
    testes_id = db.Column(db.Integer, db.ForeignKey('testando.id'))

    def __init__(self, nome_grermanica=nome_grermanica, nome_grego=nome_grego, oitavas=oitavas, tipo=tipo, tipo_do_arquivo=tipo_do_arquivo, pasta=pasta):
        self.nomeG = nome_grermanica
        self.nomeC = nome_grego
        self.oitavas = oitavas
        self.tipoN = tipo
        self.tipoA = tipo_do_arquivo
        self.pasta = pasta
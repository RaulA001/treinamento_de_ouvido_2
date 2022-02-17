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
    oitava = db.Column(db.Integer)
    tipo = db.Column(db.String)
    tipo_do_arquivo = db.Column(db.String)
    pasta = db.Column(db.String)
    testes_id = db.Column(db.Integer, db.ForeignKey('testando.id'))

    #def __init__(self, nome, oitava=oitava, nome_grermanica=nome_grermanica, nome_grego=nome_grego, tipo=tipo, tipo_do_arquivo=tipo_do_arquivo, pasta=pasta):
    #    self.nomeG = nome_grermanica
    #    self.nomeC = nome_grego
    #    self.oitava = oitava
    #    self.tipoN = tipo
    #    self.tipoA = tipo_do_arquivo
    #    self.pasta = pasta

    def __init__(self, nome, oitava=oitava, tipo_do_arquivo=tipo_do_arquivo):
        self.Nome = nome
        self.oitava = oitava
        self.tipoA = tipo_do_arquivo
        self.bulder()

    def bulder(self, obj=True):
        '''resposavel nomear notas na notção grega e germanica e separalas do seu complemento'''

        obj = True

        # notas principais
        nota = self.Nome.capitalize()

        #c = tem um complemento?
        c = False
        if 'Do' in nota or 'C' in nota or 'Dó' in nota:
            if nota[:1] in 'DoDó':
                c = True
            if obj:
                self.NotaC = 'Dó'
                self.NotaG = 'C'
        elif 'Re' in nota or 'D' in nota or 'Ré' in nota:
            if nota[:1] in 'ReRé':
                c = True
            if obj:
                self.NotaC = 'Ré'
                self.NotaG = 'D'
        elif 'Mi' in nota or 'E' in nota:
            if nota[:1] in 'MiMí':
                c = True
            if obj:
                self.NotaC = 'Mi'
                self.NotaG = 'E'
        elif 'Fá' in nota or 'F' in nota or 'Fa' in nota:
            if nota[:1] in 'FaFá':
                c = True
            if obj:
                self.NotaC = 'Fá'
                self.NotaG = 'F'
        elif 'Sol' in nota or 'G' in nota:
            if nota[:2] in 'Sol':
                c = True
            if obj:
                self.NotaC = 'Sol'
                self.NotaG = 'G'
        elif 'La' in nota or 'A' in nota or 'Lá' in nota:
            if nota[:1] in 'LaLá':
                c = True
            if obj:
                self.NotaC = 'Lá'
                self.NotaG = 'A'
        elif 'Si' in nota or 'B' in nota:
            if nota[:1] in 'SiSí':
                c = True
            if obj:
                self.NotaC = 'Si'
                self.NotaG = 'B'
        else:
            if obj:
                self.NotaC = 'Erro-Nota'
                self.NotaG = 'Erro-Nota'
            else:
                print('Não é uma nota')
        # variaçoes/Complemento
        self.tipo = c
        if c:
            if not 'Sol' in nota:
                comp = nota[2:]
            else:
                comp = nota[3:]
        else:
            comp = nota[1:]
        if obj:
            self.tipo = comp
            # nome completo
            self.NomeC = f'{self.NotaC}{self.tipo}'
            self.NomeG = f'{self.NotaG}{self.tipo}'
            self.pasta = []
        else:
            return c

    def localize(self):
        self.pasta = []
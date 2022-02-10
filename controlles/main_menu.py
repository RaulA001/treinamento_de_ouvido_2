from flask import *
from models.db import *
import json

app = Blueprint('menu', __name__, static_folder='../static', template_folder='../template')

@app.route('/', methods=['GET', 'POST'])
def menu():
    return render_template('main_menu.html')

@app.route('/teste', methods=['GET', 'POST'])
def test():
    dados = dict(request.args)
    dados = json.dumps(dados)
    print(dados)
    return render_template('test_menu.html')

@app.route('/nova_nota', methods=['GET', 'POST'])
def nova_nota():
    return render_template('nova_nota.html')

@app.route('/novo_teste', methods=['GET', 'POST'])
def novo_teste():
    return render_template('novo_teste.html')
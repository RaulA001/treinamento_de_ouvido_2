from flask import *
from models.db import *
import json

app = Blueprint('menu', __name__, static_folder='../static', template_folder='../template')

@app.route('/')
def menu():
    return render_template('main_menu.html')
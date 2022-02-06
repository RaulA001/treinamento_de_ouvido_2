from flask import *
from models.db import *
import json

app = Blueprint('configuracao', __name__, static_folder='../static', template_folder='../template')

@app.route('/')
def configuracao():
    return render_template('config_menu.html')
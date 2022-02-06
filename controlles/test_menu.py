from flask import *
from models.db import *
import json

app = Blueprint('test', __name__, static_folder='../static', template_folder='../template')

@app.route('/')
def test():
    return render_template('test_menu.html')
from flask import Flask
from models.db import *
from controlles.main_menu import app as menu
from controlles.config_menu import app as configuracao
from controlles.test_menu import app as test


#app def
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estud.db'

#Controlles
app.register_blueprint(menu, url_prefix='/menu/')
app.register_blueprint(configuracao, url_prefix='/configuracao/')
app.register_blueprint(test, url_prefix='/test/')

#init all
if __name__ == '__main__':
    db.init_app(app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['WTF_CSRF_SECRET_KEY'] = 'random key for form'
app.config['LDAP_PROVIDER_URL'] = 'ldap://localhost:389/'
app.config['LDAP_PROTOCOL_VERSION'] = 3
db = SQLAlchemy(app)

app.secret_key = '!@$#$%^&^%#@%&((^##@'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from application.auth.views import auth
app.register_blueprint(auth)

db.create_all()

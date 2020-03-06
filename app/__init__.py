from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

lm = LoginManager()
lm.init_app(app)
ma = Marshmallow(app)

from app.models import tables, produto, orcamento, orcamento_detalhe
from app.controllers import clientes
from app.routes import cliente_routes,produto_routes,orcamento_routes

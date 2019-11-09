from flask import Flask
from app.config import Configuration
from app.tabl.blueprint import tabl

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(tabl, utl_prefix='/tabl')

from app import views
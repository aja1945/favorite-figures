from flask import Flask
from yourapp.config import DEBUG, SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

from yourapp import routes
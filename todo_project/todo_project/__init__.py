from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
app.config['SECRET_KEY'] = '45cf93c4d41348cd9980674ade9a7356'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'

bcrypt = Bcrypt(app)

# Prometheus metric
REQUEST_COUNT = Counter("request_count", "Total requests")

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

# Always put Routes at end
from todo_project import routes

from flask import Flask
from flask_sqlalchemy import flask_sqlalchemy

app = Flask(__name__)

app.config.from_pyfile('config.cfg')


if __name__ == "__main__":
    app.run()
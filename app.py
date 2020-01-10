from flask import Flask
from db import init_db, session
from models.users import User

app = Flask(__name__)
init_db()


@app.route('/')
def hello_world():
    return 'Hello world!'


if __name__ == '__main__':
    app.run()

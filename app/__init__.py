from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

from app import routes


if __name__ == '__main__':
    app.run(debug=True)

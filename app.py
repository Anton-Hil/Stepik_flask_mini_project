from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return 'Hello_app'


if __name__ == '__main__':
    app.run()

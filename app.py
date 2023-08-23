from flask import Flask, render_template, url_for
from game import Player, Game

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')


@app.route('/game')
def game_page():
    return render_template('game.html')


if __name__ == '__main__':
    app.run()

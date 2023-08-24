from flask import Flask, render_template, url_for, request, redirect
from game import Player, Game, Enemy
from forms import ChooseDirectionForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/index')
def index():
    game = Game()
    game.populate_field()
    return render_template('index.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')


@app.route('/game/<int:turn_id>', methods=['get', 'post'])
def game_page(turn_id):
    game = Game()
    if game.game_over_status:
        return redirect(url_for('game_over_page'))
    if bool(turn_id):
        game.move(Enemy)
        game.update_player_status()
        return redirect(url_for('game_page', turn_id=0))
    else:
        form = ChooseDirectionForm()
        if request.method == 'GET':
            return render_template('game.html', game=game, form=form)
        if request.method == 'POST':
            direction = form.direction.data
            move_status = game.move(Player, direction)
            game.update_player_status()
            return redirect(url_for('game_page', turn_id=move_status))


@app.route('/game_over')
def game_over_page():
    player = Player()
    return render_template('game_over.html', player=player)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, url_for, request, redirect
from game import Player, Game, Enemy
from forms import ChooseDirectionForm, SettingsForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/index')
def index():
    Game()
    return render_template('index.html')


@app.route('/init')
def initialise():
    game = Game()
    game.populate_field()
    return redirect(url_for('game_page', turn_id=0))


@app.route('/settings', methods=['get', 'post'])
def settings():
    form = SettingsForm()
    if request.method == 'GET':
        return render_template('settings.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            game = Game()
            game.update_parameters(form.field_height.data,
                                   form.field_width.data,
                                   form.difficulty.data)
        return redirect(url_for('settings'))


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
            move_status = 0
            if form.validate_on_submit():
                direction = form.direction.data
                move_status = int(game.move(Player, direction))
                game.update_player_status()
            return redirect(url_for('game_page', turn_id=move_status))


@app.route('/game_over')
def game_over_page():
    player = Player()
    return render_template('game_over.html', player=player)


@app.route('/clear')
def clear():
    game = Game()
    game.reset_field()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

# Stepik_flask_mini_project
This is a final mini project for stepik flask course.
The project is mini step-by-step arcade game, where you are to navigate you way to exit on a field, filled with treasures and enemies.
## Requirements
Python 3.11+
blinker==1.6.2
click==8.1.7
colorama==0.4.6
Flask==2.3.2
Flask-WTF==1.1.1
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
Werkzeug==2.3.7
WTForms==3.0.1
## Instalation
Clone repositotory to a set python virtual env.
Run **_python -m pip install -r requirements.txt_** command to install required libraries.
## How to run
Run app.py file.

Open project page on http://127.0.0.1:5000 adress
## How to play
By clicking Start button you will start a default set game.

You may change settings by chicking Settings button and filling in the settings form.

You start a game on a random point on a field. A Player is represented with green sqare, enemies -- with red, treasures -- with gold, exit -- with cyan.
A Player view range is 3 sqares. You have to find an exit and make the highest score possible.

The game is turn based. A Player takes first turn and can move one step in any direction (if possible). To move, choose an option on a screen below and click
submit button. If the movement is impossible, you may choose another direction. Whe the movement occured, enemies take their turn and move one step in random direction.
Note: enemies can't overlap exit, treasure and another enemy position.

When you step on a treasure cell, you will score one point and a treasure will dissappear. When you reach an exit, the game is over. If a Player is hit by an enemy on any turn,
The Player is considered dead, and the game is over. You will get a message in different colors, according to the way the game has ended.

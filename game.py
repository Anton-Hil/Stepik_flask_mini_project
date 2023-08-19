from random import choice
from math import ceil


class SingletonMeta(type):
    instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instance:
            cls.instance[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls.instance[cls]


class GameObject:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col

    def move_object(self, row=0, col=0):
        self.row += row
        self.col += col


class Player(GameObject, metaclass=SingletonMeta):
    def __init__(self):
        super().__init__()
        self.key_count = 0
        self.dead = False

    def __repr__(self):
        return 'P'


class Enemy(GameObject):
    def __repr__(self):
        return 'E'


class Key(GameObject):
    def __repr__(self):
        return 'K'


class Exit(GameObject):
    def __repr__(self):
        return 'X'


class Game(metaclass=SingletonMeta):
    def __init__(self, height=20, width=20, enemies=None, keys=None):
        self.height = height
        self.width = width
        self.round_count = 0
        if enemies is None:
            self.enemies = ceil(((self.height * self.width) - 2) * 0.025)
        else:
            self.enemies = enemies
        if keys is None:
            self.keys = ceil(((self.height * self.width) - 2) * 0.0125)
        else:
            self.keys = keys
        self.field = self.__generate_field()
        self._field_status = []
        self.game_over_status = False

    def __generate_field(self):
        return [[0 for _ in range(self.width)] for _ in range(self.height)]

    @staticmethod
    def __get_position(system):
        position = choice(system)
        system.remove(position)
        return position

    def __place_object(self, cls, place):
        obj = cls(*place)
        self.field[place[0]][place[1]] = obj
        if obj not in self._field_status:
            self._field_status.append(obj)

    def __get_valid_directions(self, obj, directions):
        if isinstance(obj, Enemy):
            exceptions = (Enemy, Key, Exit)
        else:
            exceptions = ()
        valid_directions = []
        for direction in directions.keys():
            row, col = directions.get(direction)
            new_row, new_col = obj.row + row, obj.col + col
            if not 0 <= new_row < self.height or not 0 <= new_col < self.width:
                continue
            if type(self.field[new_row][new_col]) in exceptions:
                continue
            valid_directions.append(direction)
        return valid_directions

    def populate_field(self, player):
        system = [(row, col) for col in range(self.width) for row in range(self.height)]
        self.field[player.row][player.col] = Player()
        if Player() not in self._field_status:
            self._field_status.append(player)
        system.remove((player.row, player.col))
        self.__place_object(Exit, self.__get_position(system))
        for _ in range(self.keys):
            self.__place_object(Key, self.__get_position(system))
        for _ in range(self.enemies):
            self.__place_object(Enemy, self.__get_position(system))

    def move(self, cls, direction=None):
        directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
        objects = filter(lambda x: isinstance(x, cls), self._field_status)
        for obj in objects:
            valid_directions = self.__get_valid_directions(obj, directions)
            if direction is None:
                try:
                    direction = directions.get(choice(valid_directions))
                except IndexError:
                    direction = (0, 0)
            else:
                if direction not in valid_directions:
                    return False
                else:
                    direction = directions.get(direction)
            self.field[obj.row][obj.col] = 0
            obj.move_object(*direction)
            self.field[obj.row][obj.col] = obj
        return True

    def update_player_status(self):
        system = (Enemy, Key, Exit)
        for case in system:
            objects = filter(lambda x: isinstance(x, case), self._field_status)
            for obj in objects:
                if Player().row == obj.row and Player().col == obj.col:
                    if case == Enemy:
                        self.game_over_status = True
                        Player().dead = True
                    elif case == Key:
                        Player().key_count += 1
                        self._field_status.remove(obj)
                    elif case == Exit:
                        self.game_over_status = True


a = Game(5, 5)
b = Player()
a.populate_field(b)
while not a.game_over_status:
    print()
    print(*a.field, sep='\n')
    while True:
        flag = a.move(Player, input('Set direction'))
        if flag:
            break
        else:
            print('choose another direction')
    a.update_player_status()
    a.move(Enemy)
    a.update_player_status()
print()
print(*a.field, sep='\n')
print(f'Final score {Player().key_count}')

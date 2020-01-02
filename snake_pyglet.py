from pathlib import Path
import pyglet
from pyglet.window import key
from random import randrange

image = pyglet.image.load('tile.png')
image2 = pyglet.image.load('apple.png')
snake_tile = pyglet.sprite.Sprite(image)
apple = pyglet.sprite.Sprite(image2)

SPEED_X = 10
SPEED_Y = 10
TILE_SIZE = 64
SNAKE_POSITION = [(0, 0), (1, 0), (2, 0)]
FRUIT_POSITION = [(3, 3)]
direction = {'x' : 1, 'y' : 0} #global dictionary

window = pyglet.window.Window(TILE_SIZE*10, TILE_SIZE*10) #field for the snake

# TILES_DIRECTORY = Path('snake-tiles')
def direction_of_the_snake(sym, mod):
    if sym == key.LEFT:
        direction['x'] = -1
        direction['y'] = 0
    if sym == key.RIGHT:
        direction['x'] = +1
        direction['y'] = 0
    if sym == key.UP:
        direction['x'] = 0
        direction['y'] = +1
    if sym == key.DOWN:
        direction['x'] = 0
        direction['y'] = -1

def move(SNAKE_POSITION):
    starting_point = SNAKE_POSITION[- 1]
    new_point = (starting_point[0] + direction['x'], starting_point[1] + direction['y'])
    if new_point in SNAKE_POSITION:
        raise ValueError('Game over')
    else:
        if new_point == FRUIT_POSITION[0]:
            SNAKE_POSITION.append(new_point)
            del(FRUIT_POSITION[0])
            add_food()
        else:
            SNAKE_POSITION.append(new_point)
            del(SNAKE_POSITION[0])

def add_food():
    x = randrange(0, 10)
    y = randrange(0, 10)
    food_position = (x, y)
    while food_position in SNAKE_POSITION:
        x = randrange(0, 10)
        y = randrange(0, 10)
        food_position = (x, y)
    FRUIT_POSITION.append(food_position)

def tik(t):
    print(t)
    snake_tile.x = snake_tile.x + t*SPEED_X * direction['x'] #add direction
    snake_tile.y = snake_tile.y + t*SPEED_Y * direction['y']
    move(SNAKE_POSITION)
    if snake_tile.x > (window.width - snake_tile.width):
        direction['x'] = -1
    if snake_tile.y > (window.height - snake_tile.height):
        direction['y'] = -1
    if snake_tile.x < 0:
        raise ValueError('Game over')
    if snake_tile.y < 0:
        raise ValueError('Game over')

def draw_on_screen():
    window.clear()
    for item in SNAKE_POSITION:
        snake_tile.x = item[0]*TILE_SIZE
        snake_tile.y = item[1]*TILE_SIZE
        snake_tile.draw()
    for item in FRUIT_POSITION:
        apple.x = item[0]*TILE_SIZE
        apple.y = item[1]*TILE_SIZE
        apple.draw()

window.push_handlers(on_key_press=direction_of_the_snake,
    on_draw=draw_on_screen,)

pyglet.clock.schedule_interval(tik, 1)

pyglet.app.run()
print('End of the game!')

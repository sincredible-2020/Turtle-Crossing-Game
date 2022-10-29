import turtle
import time
from cars import Cars, SPEED
from player import Player, INITIAL_POSITION
from scoreboard import Scoreboard

wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.tracer(0)
wn.colormode(255)

player = Player()
cars = Cars()
scoreboard = Scoreboard()

wn.listen()
wn.onkeypress(lambda: player.forward_move(), 'Up')


timer = 0.1
is_game_on = True

while is_game_on:
    time.sleep(timer)
    wn.update()

    cars.create_cars()
    cars.movement()

    for car in cars.cars:
        if car.distance(player) < 20:
            is_game_on = False
            scoreboard.game_over()

    if player.ycor() >= 280:
        player.goto(INITIAL_POSITION)
        timer *= 0.8
        SPEED += 3
        scoreboard.update_score()





wn.exitonclick()

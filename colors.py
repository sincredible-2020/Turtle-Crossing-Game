import turtle
from turtle import Turtle
import random
import colors

color_palette = colors.color_palette

SPEED = 8

class Cars:

    def __init__(self):
        self.cars = []

    def create_cars(self):
        random_integer = random.randint(1, 5)
        if random_integer == 1:
            car = Turtle('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(color_palette))
            car.up()
            car.goto(310, random.randint(-250, 250))
            self.cars.append(car)

    def movement(self):
        for acar in self.cars:
            acar.backward(SPEED)

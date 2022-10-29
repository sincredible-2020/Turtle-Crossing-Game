from turtle import Turtle

INITIAL_POSITION = (0, -285)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.up()
        self.goto(INITIAL_POSITION)
        self.left(90)

    def forward_move(self):
        self.forward(20)

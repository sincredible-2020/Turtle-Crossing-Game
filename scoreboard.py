from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('Black')
        self.hideturtle()
        self.up()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level = {self.score} ", align="center", font=("Arial", 22, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=("Arial", 22, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

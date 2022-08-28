FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-250, 270)
        self.color("black")
        self.write(f"Level:{self.level}",align="left",font=FONT)
        self.goto(250, 270)
        self.color("black")
        self.write(self.score, align="right", font=FONT)


    def point(self):
        self.score +=1
        self.update_score()

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over",align='center',font=FONT)



from turtle import Turtle, update



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("C:\\Users\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\OOP\\snake game\\data.txt", mode = "r") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}   High Score:{self.highscore}", align="center", font=('Calibri',12,'normal'))


    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("C:\\Users\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\OOP\\snake game\\data.txt", mode = "w") as data:
                data.write(f"{self.highscore}")
           
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.penup()
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=('Calibri', 12, 'normal'))

    def count(self):
        self.score += 1
        self.update_scoreboard()







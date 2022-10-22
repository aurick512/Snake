from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 260)
        self.write(f"Score: {self.score}",align= "center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.goto(0, 260)
        self.write(f"Score: {self.score}",align= "center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align= "center", font=("Courier", 24, "normal"))

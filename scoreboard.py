from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        with open(file="data.txt") as f:
            self.high_score= int(f.read())
        self.scored()

    def scored(self):
        self.clear()
        self.write(f"Score: {self.score} high score: {self.high_score}", align='center', font=('Arial', 24, 'normal'))

    def game_reset(self):
        if self.score>self.high_score:
            with open(file="data.txt", mode="w") as file:
                file.write(str(self.score))
            self.high_score=self.score
        self.score=0
        self.scored()
    def increase_score(self):
        self.score+=1
        self.scored()


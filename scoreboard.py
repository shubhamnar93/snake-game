from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()

        self.hideturtle()
        self.goto(0, 260)
        self.i = 0
        self.scored()

        # self.write(f"Score {i}", move=True, align='right', font=('Arial', 15, 'bold'))
    def scored(self):
        self.clear()
        self.write(f"Score: {self.i}", align='center', font=('Arial', 24, 'normal'))

        self.i += 1
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over.", align='center', font=('Arial', 24, 'bold'))

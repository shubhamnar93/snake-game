import turtle as t
class Snake:

    def __init__(self):
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments=self.setup_snake()

    def setup_snake(self):
        segments=[]
        for position in self.starting_position:
            new_segment = t.Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            segments.append(new_segment)
        return segments

    def reset_snake(self):
        for seg in self.segments[3:]:
            seg.goto(1000,1000)
        del self.segments[3:]
        self.segments[0].goto(0,0)


    def extend(self):
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)

    def snake_animation(self):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
        self.segments[0].fd(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)


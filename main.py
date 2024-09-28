import time
import turtle as t
from snake import Snake
from food import Food
from scoreboard import ScoreBoard



snake=Snake()
screen=t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("snake game")
screen.tracer(0)

game_on=True
food=Food()
score=ScoreBoard()
i=3

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

while game_on:
    snake.snake_animation()
    screen.update()
    time.sleep(0.1)

    if snake.segments[0].distance(food) < 20:
        food.food_eaten()
        snake.extend()
        score.increase_score()

    if snake.segments[0].xcor()> 280 or snake.segments[0].xcor()< -280 or snake.segments[0].ycor()> 290 or snake.segments[0].ycor()< -290:
        score.game_reset()
        snake.reset_snake()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment.pos())<10:
            score.game_reset()
            snake.reset_snake()






screen.exitonclick()
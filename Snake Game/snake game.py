from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
score_count = Scoreboard()

screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score_count.count()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        score_count.reset_score()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_count.reset_score()
            snake.reset()




screen.setup(width=600,height=600)
screen.exitonclick()

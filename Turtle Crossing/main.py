import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
score_count = Scoreboard()
screen.listen()

screen.onkey(player.up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()


   #detect collision with car
    for i in car.all_cars:
        if i.distance(player) < 20:
            score_count.game_over()
            game_is_on = False

    if player.finish():
        score_count.update_score()
        score_count.point()
        player.start()
        score_count.level_up()
        car.increase_level()










screen.exitonclick()
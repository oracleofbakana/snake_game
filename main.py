from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game developed in Python")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.11)
    snake.move()

#   detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


#  Detect collision with tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

#  Detect collision with the tail
    if snake.head.xcor() > 270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()

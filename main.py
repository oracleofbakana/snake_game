from turtle import Screen
import time
from food import Food
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game developed in Python")
screen.tracer(0)

snake = Snake()
food = Food()

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

    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()

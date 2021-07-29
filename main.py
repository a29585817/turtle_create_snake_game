from turtle import Screen
import time

from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
hight = score.hight_score





game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.get_point()
    #Detect collision withwall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
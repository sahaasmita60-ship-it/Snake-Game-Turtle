from snake import Snake
from food import Food
from score import Score
from turtle import Turtle, Screen
import time
t=Turtle()
screen=Screen()
screen.tracer(0)
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.listen()
snake=Snake()
food=Food()
snake.turtlecreate()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on=True
scor=0
food.foodcreate()
score=Score()

while game_is_on==True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.all_t[0].distance(food)<20:
     scor=scor+1
     food.again()
     score.incscore(scor)
     snake.extend()

    if 300<snake.all_t[0].xcor() or snake.all_t[0].xcor()<-300 or 300<snake.all_t[0].ycor() or snake.all_t[0].ycor()<-300:
     score.over()
     game_is_on=False

    if snake.tail()==True:
     score.over()
     game_is_on=False
screen.exitonclick()
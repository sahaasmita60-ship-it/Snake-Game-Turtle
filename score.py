from snake import Snake
from food import Food
from turtle import Turtle, Screen
import time
snake=Snake()
food=Food()
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.createscore()      
    def createscore(self):
        self.clear()
        self.write(f"Score={self.score}", align="center",font=("Arial",12,"normal"))
    def incscore(self,score):

          self.score+=1
          self.createscore()
    def over(self):

          self.clear()
          self.write(f"Game over", align="center",font=("Arial",12,"normal"))
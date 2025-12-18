from turtle import Turtle,Screen
import random
class Food(Turtle):
    def __init__(self):
      super().__init__()
    def foodcreate(self):
      self.shape("circle")
      self.color("green")
      self.penup()
      self.speed("fastest")
      self.shapesize(0.5,0.5)
      self.foodx=random.randint(-280,280)
      self.foody=random.randint(-280,280)
      self.goto(self.foodx,self.foody)
    def again(self):
      self.foodx=random.randint(-280,280)
      self.foody=random.randint(-280,280)
      self.goto(self.foodx,self.foody)
    

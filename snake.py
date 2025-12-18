from turtle import Turtle, Screen
import time
class Snake():
 def __init__(self):
  self.x=0
  self.all_t=[]
  self.f=-40
 def turtlecreate(self):
   while self.x>-41:
    self.t=Turtle()
    self.t.penup()
    self.t.shape("square")
    self.t.color("white")
    self.t.speed("fastest")
    self.t.goto(self.x,0)
    self.x=self.x-20
    self.all_t.append(self.t)
    self.game_is_on=True
 def extend(self):
    
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.speed("fastest")
    new_segment.goto(self.all_t[-1].position())
    self.all_t.append(new_segment)

 def tail(self):
    head=self.all_t[0]
    for i in self.all_t[1:]:
      if head.distance(i)<10:
         game_over = Turtle()
         game_over.hideturtle()
         game_over.penup()
         game_over.color("white")
         game_over.goto(0, 0)
         return True
    

 def move(self):
   for t in range(len(self.all_t)-1,0,-1):
        self.new_x=self.all_t[t-1].xcor()
        self.new_y=self.all_t[t-1].ycor()
        self.all_t[t].goto(self.new_x,self.new_y)
   self.all_t[0].forward(20)
 def up(self):
    self.all_t[0].setheading(90)
 def down(self):
    self.all_t[0].setheading(270)
 def right(self):
    self.all_t[0].setheading(0)
 def left(self):
    self.all_t[0].setheading(180)

    
  
 
 











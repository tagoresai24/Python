from turtle import Turtle
from turtle import Screen

saru = Turtle()
saru.shape("turtle")
saru.color("orange")

def draw(n):
    angle = 360/n
    for i in range(n):
        saru.forward(100)
        saru.right(angle)
    for i in range(n):
        saru.forward(100)
        saru.left(angle)    
        
for i in range(3,11):
    draw(i)        
     
    

    
    







screen = Screen()
screen.exitonclick()

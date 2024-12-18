from turtle import Turtle, Screen   
a=Turtle()
screen=Screen()
a.speed("fastest")
def move():
    a.forward(50)
def back():
    a.backward(50)
def left():
    new = a.heading() + 10
    a.setheading(new)
def right():
    new = a.heading() - 10
    a.setheading(new) 
def clear():
    a.clear()
    a.penup()
    a.home() 
    a.pendown()              
    
screen.listen()
screen.onkey(key="w", fun=move)
screen.onkey(key="s", fun=back)
screen.onkey(key="d", fun=left)
screen.onkey(key="a", fun=right)
screen.onkey(clear,"c")


screen.exitonclick()    
from turtle import Turtle , Screen
import random
all_turtles=[]


is_rance_on = False
b=Screen()
b.setup(width=500, height=400)
user_input = b.textinput(title="Make Your Bet", prompt="Which color turtle will win:  ")
colors=["red","orange","yellow","blue","green","purple"]
y_positions = [-70,-40,-10,20,50,80]
for turtle_index in range(0,6):
    a=Turtle(shape="turtle")
    a.penup()
    a.goto(x=-230 ,y=y_positions[turtle_index])
    a.color(colors[turtle_index])
    all_turtles.append(a)
    
if user_input:
    is_rance_on = True
    
while is_rance_on:
    
    
    for i in all_turtles:
        
        if i.xcor()>230:
            is_rance_on=False
            win=i.pencolor()
            if win == user_input:
                print("You won")
            else:
                print(f"The {win} color turtle won")  
                  
        distance = random.randint(0,10)     
        i.forward(distance)
        
     
      


b.exitonclick()    

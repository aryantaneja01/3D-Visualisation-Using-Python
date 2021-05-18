from turtle import *
from random import randint
speed(0)
penup()
goto(-140,140)
for step in range(15):
    write(step)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
    
ada=Turtle()
ada.color('Red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()

for turn in range(50):
    ada.forward(randint(1,5))
    
bob=Turtle()
bob.color('Blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160,170)

coc=Turtle()
coc.color('Green')
coc.shape('turtle')
coc.penup()
coc.goto(-160,40)
coc.pendown()

for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    coc.forward(randint(1,5))
    


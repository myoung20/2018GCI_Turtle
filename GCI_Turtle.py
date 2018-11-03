import turtle
import random

i=0
turtle.speed(100)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'violet', 'cyan', 'black']
while i<random.randint(20,40):
    turtle.width(random.randint(2,5))
    turtle.pencolor(random.choice(colors))
    turtle.circle(random.randint(1,100))
    turtle.pu()
    turtle.forward(random.randint(-100,100))
    turtle.setheading(random.randint(1,360))
    turtle.pd()
    i=i+1


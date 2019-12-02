from pylab import *
from turtle import *

bgcolor('black')
shape('turtle')
color('seagreen')
speed(0)

for i in range(10000):
    forward(10)
    vinkel = randint(0,360)
    right(vinkel)
    
exitonclick()

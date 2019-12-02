from turtle import *
from pylab import *

bgcolor('black')
color('cyan') # Fargelegger
shape('turtle') # Gir sirkelform til objektet
speed(0)        # Endrer farten til objektet
N = 1000 # Antall ganger pekeren skal bevege seg
avstand = 10 # Hvor langt pekeren går mellom hver gang

for i in range(N):
    vinkel = randint(0,360) # Tilfeldig vinkel hver gang
    right(vinkel) # Snur tilfeldig vinkel
    forward(avstand) # Går framove
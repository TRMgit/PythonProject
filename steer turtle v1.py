from turtle import *
x = 0
speed(0)
sd = 0

penup()
goto(-100, 0)
pendown()
for i in range(4):
  forward(10)
  right(90)

color("red")
shape("turtle")
pensize(3)

penup()
goto(0, 0)
pendown()

speed(1)

begin_fill()
fillcolor("blue")

for i in range(4):
  forward(40)
  right(90)
  
while True:
 
  x = input("wasd? penup? pendown? TurtSpeed?")
  if x == "w":
      forward(10 + sd)
  elif x == "s":
      back(10 + sd)
  elif x == "d":
      right(10 + sd)
  elif x == "a":
      left(10 + sd)
  elif x == "penup":
      penup()
  elif x == "pendown":
      pendown()
  elif x == "TurtSpeed":
      sd = (speed + 10)


     # end_fill()
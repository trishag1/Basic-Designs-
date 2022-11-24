"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

#t = turtle.Turtle()
#for c in ['red', 'green', 'blue', 'yellow']:
 #   t.color(c)
 #   t.forward(75)
 #   t.left(90)

# an orange right triangle, outline color: brown, background: red
#pensize(), pencolor(), fillcolor(), speed() functions
t = turtle.Turtle()
turtle.bgcolor("red")  
t.pencolor("brown")
t.fillcolor("orange")
t.pensize(4)
t.speed(2)
t.begin_fill()
#forming the right triangle
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()

color_set=['black','pink', 'purple','yellow','blue']
t.pensize(4)
t.penup()
t.setposition(60,20)
t.pendown()
for i in range(5):
     t.pencolor(color_set[i])
     t.forward(190)
     t.right(144)
#to draw upward
t.penup()
#adjusting position of circle
t.setposition(80,-140)
#to draw downward
t.pendown()
t.hide()
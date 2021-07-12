import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
turtoise = turtle.Pen()
turtle.bgcolor("black")
turtoise.speed(30)
for x in range(360):
    turtoise.pencolor(colors[x%6])
    turtoise.width(x/100 + 1)
    turtoise.forward(x)
    turtoise.left(59)
